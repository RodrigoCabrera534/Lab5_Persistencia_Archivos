# integrante3_agregar.py

def ingresar_contacto():
    nombre = input('Ingresa el nombre: ')
    telefono = input('Ingresa el teléfono: ')
    return nombre, telefono


def agregar_contacto(nombre, telefono):
    with open('contactos.txt', 'a', encoding='utf-8') as archivo:
        archivo.write(f'{nombre},{telefono}\n')
    print('Contacto agregado correctamente en contactos.txt')


# Ejecución
nombre, telefono = ingresar_contacto()
agregar_contacto(nombre, telefono)