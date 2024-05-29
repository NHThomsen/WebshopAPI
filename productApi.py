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