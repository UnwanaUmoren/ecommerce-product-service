import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

def test_homepage():
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    assert response.data == b"Welcome to Wannie's E-commerce website"

def test_products():
    client = app.test_client()
    response = client.get('/products')
    assert response.status_code == 200
    assert response.json['name'] == 'Sweatshirt'
    assert response.json['price'] == '£30.99'
    assert len(response.json) == 3
    assert response.json == [
        {'id': 1, 'name':'Sweatshirt', 'price':'£30.99'},
        {'id': 2, 'name':'Jeans', 'price':'£49.99'},
        {'id': 3, 'name':'Jacket', 'price':'£89.99'}
    ]


