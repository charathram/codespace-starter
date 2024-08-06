from fastapi import FastAPI
from app.api.endpoints import magazines, plans, subscriptions, users, token
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(token.router, prefix="/token", tags=["token"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(magazines.router, prefix="/magazines", tags=["magazines"])
app.include_router(plans.router, prefix="/plans", tags=["plans"])
app.include_router(
    subscriptions.router, prefix="/subscriptions", tags=["subscriptions"]
)
