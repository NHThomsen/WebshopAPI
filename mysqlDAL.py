import mysql.connector
import product

class MySQLDAL:
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost",user="root",password="Pa$$w0rd")
    
    def GetAllProducts(self):
        mydb = mysql.connector.connect(host="localhost",user="root",password="Pa$$w0rd")
        mycursor = mydb.cursor()
        mycursor.execute("CALL `webshop`.`GetAllProducts`()")
        myresult = mycursor.fetchall()
        products = []
        for prod in myresult:
            newProduct = product.Product(prod[0],prod[1],prod[2])
            products.append(newProduct)
        mycursor.close()
        return products
    
    def GetProductById(self, id):
        returnProduct = None
        mydb = mysql.connector.connect(host="localhost",user="root",password="Pa$$w0rd")
        mycursor = mydb.cursor()
        args =(id,)
        mycursor.callproc('webshop.GetProductById',args)
        for result in mycursor.stored_results():
            resultProduct = result.fetchone()
            if resultProduct != None:
                returnProduct = product.Product(resultProduct[0],resultProduct[1],resultProduct[2])
        mycursor.close()
        return returnProduct
    
    def InsertProduct(self, name, price):
        mydb = mysql.connector.connect(host="localhost",user="root",password="Pa$$w0rd")
        mydb.autocommit = True
        mycursor = mydb.cursor()
        args = (name,price)
        mycursor.callproc('webshop.InsertProduct',args)
        mycursor.close()

    def UpdateProduct(self, id, name, price):
        mydb = mysql.connector.connect(host="localhost",user="root",password="Pa$$w0rd")
        mydb.autocommit = True
        mycursor = mydb.cursor()
        mycursor.callproc('webshop.UpdateProduct',args=(id,name,price))
        mycursor.close() 