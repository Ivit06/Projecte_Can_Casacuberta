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
            f.close()
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

