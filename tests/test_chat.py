import pytest
from src.backend.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_chat_endpoint(client):
    response = client.post('/chat', json={'question': 'Hello'})
    assert response.status_code == 200
    assert 'answer' in response.json
