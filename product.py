from json import JSONEncoder
import decimal

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class ProductEncoder(JSONEncoder):
    def default(self,o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return o.__dict__