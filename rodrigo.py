# integrante1_escribir.py


def ingresar_contacto():
    nombre = input('Ingresa el nombre: ')
    telefono = input('Ingresa el teléfono: ')
    return nombre, telefono


def escribir_contacto(nombre, telefono):
    with open('contactos.txt', 'w', encoding='utf-8') as archivo:
        archivo.write(f'{nombre},{telefono}\n')
    print('Contacto guardado correctamente en contactos.txt')


# Ejecución
nombre, telefono = ingresar_contacto()
escribir_contacto(nombre, telefono)
