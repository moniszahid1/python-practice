import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_redirects_to_login(client):
    response = client.get('/')
    assert response.status_code == 302

def test_login_page_loads(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_login_with_correct_credentials(client):
    response = client.post('/login', data={'username': 'admin', 'password': 'secret123'})
    assert response.status_code == 302
    assert '/dashboard' in response.headers['Location']

def test_login_with_wrong_credentials(client):
    response = client.post('/login', data={'username': 'wrong', 'password': 'wrong'})
    assert response.status_code == 200
    assert b'Invalid username or password' in response.data

def test_dashboard_requires_login(client):
    response = client.get('/dashboard')
    assert response.status_code == 302

def test_logout_clears_session(client):
    client.post('/login', data={'username': 'admin', 'password': 'secret123'})
    response = client.get('/logout')
    assert response.status_code == 302