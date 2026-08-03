from uuid import uuid4


def create_test_user(client):
    email = f"user_{uuid4().hex}@example.com"

    payload = {
        "name": "Test User",
        "email": email,
        "password": "Password@123"
    }

    response = client.post(
        "/auth/register",
        json=payload
    )

    return email, payload["password"]


def test_register_user(client):

    email = f"test_{uuid4().hex}@example.com"

    payload = {
        "name": "Test User",
        "email": email,
        "password": "Password@123"
    }

    response = client.post(
        "/auth/register",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["email"] == email



def test_register_duplicate_email(client):

    email, password = create_test_user(client)

    payload = {
        "name": "Test User",
        "email": email,
        "password": password
    }

    response = client.post(
        "/auth/register",
        json=payload
    )

    assert response.status_code == 400



def test_login_success(client):

    email, password = create_test_user(client)

    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": password
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"



def test_login_wrong_password(client):

    email, password = create_test_user(client)

    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": "WrongPassword123"
        }
    )

    assert response.status_code == 401