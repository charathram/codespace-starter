from fastapi import APIRouter, Depends, HTTPException, status
from jose import JWTError, jwt as jose_jwt
from sqlalchemy.orm import Session
from app.core import jwt
from app.core.config import settings
from app.schemas.user import UserCreate, UserLogin, UserOut, UserInDB
from app.schemas.token import Token, TokenData
from app.crud import user as crud_user
from app.dependencies import get_db, get_current_user, oauth2_scheme
from app.core.security import verify_password, get_password_hash
from app.core.jwt import create_access_token, create_refresh_token

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = crud_user.create_user(db, user, hashed_password)
    return db_user

@router.post("/login", response_model=Token)
def login_user(form_data: UserLogin, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_username(db, username=form_data.username)
    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": db_user.username})
    refresh_token = create_refresh_token(data={"sub": db_user.username})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.post("/reset-password")
def reset_password(email: str, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    # Assuming a password reset logic here
    new_password = "new_password"  # Replace with actual password reset logic
    db_user.hashed_password = get_password_hash(new_password)
    db.commit()
    db.refresh(db_user)
    return {"msg": "Password reset successful"}


@router.delete("/deactivate/{username}")
def deactivate_user(username: str, db: Session = Depends(get_db), current_user: UserInDB = Depends(get_current_user)):
    db_user = crud_user.get_user_by_username(db, username=username)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.is_active = False
    db.commit()
    db.refresh(db_user)
    return {"msg": "User deactivated"}

@router.post("/token/refresh", response_model=Token)
def refresh_token(refresh_token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jose_jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = crud_user.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    new_access_token = create_access_token(data={"sub": user.username})
    new_refresh_token = create_refresh_token(data={"sub": user.username})
    return {"access_token": new_access_token, "refresh_token": new_refresh_token, "token_type": "bearer"}


@router.get("/me", response_model=UserOut)
def get_current_user_profile(current_user: UserInDB = Depends(get_current_user)):
    return current_user
