import requests

def testGetAllBooks():
    url = "http://127.0.0.1:5000/products"
    response = requests.get(url)

    assert response.status_code == 200

def testGetProductByIdSuccess():
    url = "http://127.0.0.1:5000/products/1"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data,dict)
    assert "id" in data
    assert "name" in data
    assert "price" in data