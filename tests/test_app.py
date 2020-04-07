import os
import pytest

from server.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client

def test_bad_route(client):
    rv = client.get("/bad-route")
    assert rv.status_code == 400

def test_root_route(client):
    rv = client.get("/")
    assert rv.status_code == 200
    
    obj = rv.get_json()
    assert obj['message'] == 'success'
    assert obj['local_path'] == './test_dir/'
    assert len(obj['contents']) == 3

def test_subdir_route(client):
    rv = client.get("/sub_dir")
    assert rv.status_code == 200
    
    obj = rv.get_json()
    assert len(obj['contents']) == 0
    
def test_perms(client):
    rv = client.get("/")
    obj = rv.get_json()
    # and so on...