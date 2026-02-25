import pytest
from app import app

@pytest.fixture
def client():
    """
    Flask test client fixture.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """
    Test that the index page loads correctly.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b'Unit Converter' in response.data

def test_length_conversion(client):
    """
    Test length conversion from meter to kilometer.
    """
    response = client.post('/length', data={
        'value': '1000',
        'from_unit': 'meter',
        'to_unit': 'kilometer'
    })
    assert response.status_code == 200
    assert b'Result: 1.0' in response.data

def test_weight_conversion(client):
    """
    Test weight conversion from kilogram to gram.
    """
    response = client.post('/weight', data={
        'value': '2',
        'from_unit': 'kilogram',
        'to_unit': 'gram'
    })
    assert response.status_code == 200
    assert b'Result: 2000.0' in response.data

def test_temperature_conversion(client):
    """
    Test temperature conversion from Celsius to Fahrenheit.
    """
    response = client.post('/temperature', data={
        'value': '0',
        'from_unit': 'Celsius',
        'to_unit': 'Fahrenheit'
    })
    assert response.status_code == 200
    assert b'Result: 32.0' in response.data

def test_invalid_length_unit(client):
    """
    Test invalid length unit handling.
    """
    response = client.post('/length', data={
        'value': '10',
        'from_unit': 'invalid',
        'to_unit': 'meter'
    })
    assert response.status_code == 200
    assert b'Error' in response.data

def test_invalid_weight_unit(client):
    """
    Test invalid weight unit handling.
    """
    response = client.post('/weight', data={
        'value': '10',
        'from_unit': 'invalid',
        'to_unit': 'gram'
    })
    assert response.status_code == 200
    assert b'Error' in response.data

def test_invalid_temperature_unit(client):
    """
    Test invalid temperature unit handling.
    """
    response = client.post('/temperature', data={
        'value': '10',
        'from_unit': 'invalid',
        'to_unit': 'Celsius'
    })
    assert response.status_code == 200
    assert b'Error' in response.data