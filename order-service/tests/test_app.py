import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health_endpoint():
    """Test health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'healthy'

def test_get_orders():
    """Test get all orders"""
    response = client.get('/api/orders')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
