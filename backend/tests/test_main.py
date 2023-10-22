"""test file for main.py"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cinematch.backend.main import app, get_db

client = TestClient(app)

test_db_url = "sqlite:///./test.db"
engine = create_engine(test_db_url)


# Override the get_db dependency
@pytest.fixture
def override_get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


def test_signup():
    response = client.post("/signup/", json={"username": "testuser"})
    assert response.status_code == 200
    assert response.json() == {"username": "testuser", "id": 1}


def test_login():
    response = client.post("/login/", data={"username": "testuser"})
    assert response.status_code == 200
    assert response.json() == {"message": "Logged in as testuser"}
