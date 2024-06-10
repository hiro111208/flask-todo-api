import json


def test_register(client):
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 201
    assert response.get_json()['msg'] == 'User registered successfully'


def test_login(client):
    # First, register a user
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })

    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 200
    assert 'access_token' in response.get_json()


def test_invalid_login(client):
    response = client.post('/login', json={
        'username': 'nonexistentuser',
        'password': 'wrongpass'
    })
    assert response.status_code == 401
    assert response.get_json()['msg'] == 'Invalid credentials'
