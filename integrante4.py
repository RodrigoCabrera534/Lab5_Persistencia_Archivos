# integrante4_buscar.py

def buscar_contacto(nombre_buscar):
    encontrado = False
    try:
        with open('contactos.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                datos = linea.strip().split(',')
                if datos[0].lower() == nombre_buscar.lower():
                    print(f'Contacto encontrado: {datos[0]} - {datos[1]}')
                    encontrado = True
        if not encontrado:
            print(f'No se encontró ningún contacto con el nombre "{nombre_buscar}".')
    except FileNotFoundError:
        print('No se encontró el archivo contactos.txt')


# Ejecución
nombre = input('Ingresa el nombre a buscar: ')
buscar_contacto(nombre)