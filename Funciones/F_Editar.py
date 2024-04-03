def editar_libro(archivo, isbn_buscar, nuevo_contenido):
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print("El archivo no existe.")
        return

    encontrado = False
    for i, linea in enumerate(lineas):
        if isbn_buscar in linea:
            lineas[i] = nuevo_contenido + '\n'
            encontrado = True
            break
    
    if not encontrado:
        print("ISBN no encontrado.")
        return
    
    try:
        with open(archivo, 'w') as f:
            f.writelines(lineas)
    except:
        print("Error al escribir en el archivo.")

# Función para solicitar al usuario el ISBN del libro a editar
def solicitar_isbn():
    while True:
        isbn = input("Por favor, introduzca el ISBN del libro que desea editar (o 'salir' para salir): ")
        if isbn.lower() == 'salir':
            return None
        if len(isbn) > 0:
            return isbn
        else:
            print("Por favor, introduzca un ISBN válido.")

archivo = "../Llibres.txt"  

isbn_a_editar = solicitar_isbn()
if isbn_a_editar:
    nuevo_contenido = input("Introduzca el nuevo contenido del libro en el formato Título|Autor|Año|Género|ISBN: ")
    editar_libro(archivo, isbn_a_editar, nuevo_contenido)
else:
    print("Saliendo del programa.")
