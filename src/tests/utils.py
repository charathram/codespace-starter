import random
from app.schemas.user import UserCreate
from app.schemas.magazine import MagazineCreate


def create_user(client, base_username: str, base_email: str, password: str):
    unique_id = random.randint(1000, 9999)
    username = f"{base_username}{unique_id}"
    email = f"{base_email.split('@')[0]}{unique_id}@{base_email.split('@')[1]}"
    
    user_data = UserCreate(username=username, email=email, password=password)
    response = client.post("/users/register", json=user_data.model_dump())
    assert response.status_code == 200, f"Response status code: {response.status_code}, Response body: {response.text}"
    print(f"Created user: {username}, {email}, {password}")
    return username, email


def login_user(client, username: str, password: str):
    response = client.post("/users/login", json={"username": username, "password": password})
    assert response.status_code == 200, f"Response status code: {response.status_code}, Response body: {response.text}"
    return response.json()["access_token"]


def create_plan(client, headers):
    response = client.post("/plans/", json={
        "title": "Monthly",
        "description": "Monthly subscription plan",
        "renewal_period": 1
    }, headers=headers)
    assert response.status_code == 200, f"Response status code: {response.status_code}, Response body: {response.text}"
    return response.json()


def create_magazine(client, headers, name_suffix):
    response = client.post("/magazines/", json={
        "name": f"Tech Weekly {name_suffix}",
        "description": "A weekly tech magazine",
        "base_price": 5.0,
        "discount_quarterly": 0.1,
        "discount_half_yearly": 0.2,
        "discount_annual": 0.3
    }, headers=headers)
    assert response.status_code == 200, f"Response status code: {response.status_code}, Response body: {response.text}"
    return response.json()