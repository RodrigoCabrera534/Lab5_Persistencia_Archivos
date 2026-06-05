# integrante2_leer.py

def mostrar_contactos():
    try:
        with open('contactos.txt', 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print('El archivo está vacío.')
            else:
                print('--- Lista de contactos ---')
                for i, linea in enumerate(lineas, start=1):
                    datos = linea.strip().split(',')
                    print(f'{i}. Nombre: {datos[0]}  |  Teléfono: {datos[1]}')
    except FileNotFoundError:
        print('No se encontró el archivo contactos.txt')


# Ejecución
mostrar_contactos()

