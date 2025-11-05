import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

def test_hello():
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    assert response.data == b"Hello there just playing with Flask"


