import json
import pytest
from run import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_empty_list(client):
    rv = client.get('/items')
    assert rv.status_code == 200
    assert rv.get_json() == []

def test_add_and_list(client):
    rv = client.post('/items', json={'name': 'foo'})
    assert rv.status_code == 201
    assert rv.get_json()['name'] == 'foo'

    rv2 = client.get('/items')
    assert rv2.status_code == 200
    assert any(item['name'] == 'foo' for item in rv2.get_json())
