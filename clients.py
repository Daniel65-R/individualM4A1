import json
import time
from helpers import clear, update, open_file
from classes import Client

# Cargar los datos de clientes desde el archivo
clients = open_file('clients.json')

def client_view():
    clients_updated = open_file('clients.json')
    for client in clients_updated: 
        print('*********************************************')
        print(f'ID: {client["id"]} / Nombre: {client["name"]} / Apellido: {client["last_name"]} / Edad: {client["age"]} / Contraseña: {client["password"]}')
        print('*********************************************')
        time.sleep(1)

def add_client():
    while True:
        name = input('Ingrese Nombre: ')
        if name.isalpha():
            break
        print("Debe ingresar un nombre válido con solo letras.")

    while True:
        last_name = input('Ingrese Apellido: ')
        if last_name.isalpha():
            break
        print("Debe ingresar un apellido válido con solo letras.")
    
    while True:
        age = input('Ingrese Edad: ')
        if age.isdigit() and int(age):
            break
        print("Debe ingresar una edad válida en números enteros.")
    password = input('Ingrese Contraseña: ')
    new_client: Client = Client( name, last_name, age, password).new_client()
    time.sleep(2)
    clear()
    client_view()

# Función para eliminar un cliente según su ID
def del_client():
    client_view()
    id = input('Ingrese ID a eliminar: ')
    client: Client = Client()
    client.del_client(id)
    clear()
    client_view()
