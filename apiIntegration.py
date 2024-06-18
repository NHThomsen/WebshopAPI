import requests

def testGetAllBooks():
    url = "http://127.0.0.1:5000/products"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data,list)

def testGetProductById():
    url = "http://127.0.0.1:5000/products/1"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data,dict)
    assert "id" in data
    assert "name" in data
    assert "price" in data

def testGetProductByIdFailure():
    url = "http://127.0.0.1:5000/products/99999999"
    response = requests.get(url)

    assert response.status_code == 404

    assert response.headers["Content-Type"] == "application/json"

    data = response.json()
    assert "Error" in data
    assert data["Error"] == "Product not found"

def testInsertProduct():
    url = "http://127.0.0.1:5000/products"
    insertProduct = {
        'name':'Integration product - pytest',
        'price':'0.02'}
    response = requests.post(url,json=insertProduct)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data,dict)
    assert "Product" in data
    assert data["Product"] == "inserted"

def testInsertProductFailure():
    url = "http://127.0.0.1:5000/products"
    insertProduct = {
        'name':'Integration product',
        'price':'abc'}
    response = requests.post(url,json=insertProduct)

    assert response.status_code == 400

    data = response.json()
    assert isinstance(data,dict)
    assert "Product" in data
    assert data["Product"] == "not inserted"