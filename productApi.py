from flask import Flask, jsonify
import mysqlDAL
import json
import product

app = Flask(__name__)

DAL = mysqlDAL.MySQLDAL()

@app.route("/products",methods=['GET'])
def getAllProducts():
    allProducts = DAL.GetAllProducts()
    if len(allProducts) > 0:
        return json.dumps(allProducts,indent=4,cls=product.ProductEncoder)
    else:
        return jsonify({'Error':'No products found'}), 204
    
@app.route("/products/<int:id>",methods=['GET'])
def getProductById(id: int):
    getProduct = DAL.GetProductById(id)
    if getProduct != None:
        return json.dumps(getProduct,indent=4,cls=product.ProductEncoder)
    else:
        return jsonify({'Error':'Product not found'}), 404