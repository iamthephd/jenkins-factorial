from fastapi.testclient import TestClient
import pytest
from app import app, calculate_factorial

client = TestClient(app)

def test_calculate_factorial():
    assert calculate_factorial(0) == 1
    assert calculate_factorial(1) == 1
    assert calculate_factorial(5) == 120
    assert calculate_factorial(10) == 3628800
    
    with pytest.raises(ValueError):
        calculate_factorial(-1)

def test_factorial_api():
    response = client.post("/api/factorial", json={"number": 5})
    assert response.status_code == 200
    assert response.json() == {"number": 5, "factorial": 120}
    
    response = client.post("/api/factorial", json={"number": -1})
    assert response.status_code == 400
    
    response = client.post("/api/factorial", json={"number": 0})
    assert response.status_code == 200
    assert response.json() == {"number": 0, "factorial": 1}