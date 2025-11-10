import pytest
from app.routes import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"All News Articles" in rv.data

def test_clusters(client):
    rv = client.get("/clusters")
    assert rv.status_code == 200

import pytest
from app.routes import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"All News Articles" in rv.data

def test_clusters(client):
    rv = client.get("/clusters")
    assert rv.status_code == 200

