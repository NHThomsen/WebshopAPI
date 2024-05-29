import mysql.connector
import product

class MySQLDAL:
    mydb = None

    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost",user="root",password="Pa$$w0rd")
    
    def GetAllProducts(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM webshop.Products")
        myresult = mycursor.fetchall()
        products = []
        for prod in myresult:
            newProduct = product.Product(prod[0],prod[1],prod[2])
            products.append(newProduct)
        return products