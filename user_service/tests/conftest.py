import pytest
from app import app as user_app
from app import mongo


@pytest.fixture
def client():
    with user_app.test_client() as client:
        with user_app.app_context():
            # Setup database before tests
            mongo.db.users.delete_many({})
        yield client
        # Clean up database after tests
        mongo.db.users.delete_many({})
