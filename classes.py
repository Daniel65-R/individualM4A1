from helpers import open_file, update


class Client:
    name: str
    last_name: str
    age: int
    password: str

    def __init__(self, name=None, last_name=None, age=None, password=None):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.password = password

    def new_client(self):
        clients = open_file('clients.json')
        new_client = {'id': len(clients)+1, 'name': self.name,
                      'last_name': self.last_name, 'age': self.age, 'password': self.password}
        clients.append(new_client)
        update(clients, 'clients.json')

    def del_client(self, id):
        clients = open_file('clients.json')
        for i, client in enumerate(clients):
            if client["id"] == int(id):
                del clients[i]
                update(clients, 'clients.json')
                break

class Product:
    name: str
    stock: int

    def __init__(self, name=None, stock=None):
        self.name = name
        self.stock = stock

    def new_product(self):
        products = open_file('store.json')
        new_product = {'id': len(products)+1, 'name': self.name, 'stock': self.stock}
        products.append(new_product)
        update(products, 'store.json')