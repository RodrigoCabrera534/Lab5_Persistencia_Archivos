import pickle

def guardar_binario(contactos):
    with open("contactos.pkl", "wb") as archivo:
        pickle.dump(contactos, archivo)
    print("Contactos guardados en archivo binario contactos.pkl")

def cargar_binario():
    try:
        with open("contactos.pkl", "rb") as archivo:
            contactos = pickle.load(archivo)

        print("--- Contactos cargados desde archivo binario ---")
        for c in contactos:
            print(f"Nombre: {c['nombre']} | Teléfono: {c['telefono']}")

    except FileNotFoundError:
        print("No se encontró el archivo binario contactos.pkl")

lista = [
    {"nombre": "Ana", "telefono": "999123456"},
    {"nombre": "Luis", "telefono": "998456789"},
    {"nombre": "María", "telefono": "997334455"}
]

guardar_binario(lista)
cargar_binario()