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

def test_update_item_success(client):
    # First, add an item so there’s something to update
    client.post('/items', json={'name': 'old'})
    # Now update it
    rv = client.put('/items/1', json={'name': 'new'})
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['id'] == 1
    assert data['name'] == 'new'

def test_update_item_not_found(client):
    # Try updating a non‐existent ID
    rv = client.put('/items/999', json={'name': 'nope'})
    assert rv.status_code == 404
    assert rv.get_json() == {'error': 'Not found'}

