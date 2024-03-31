def eliminar_titulo (archivo):
    try:
        titulo_libro = input("Introduce el título del libro que quieres eliminar: ")
        with open(archivo, 'r') as a:
            contenido = a.readlines()
        with open(archivo, 'w') as a:
            for linea in contenido:
                if linea.strip("\n") != titulo_libro:
                    a.write(linea)
    except FileNotFoundError:
        print("El archivo 'archivo.txt' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    else:
        print(f"El libro con el título {titulo_libro} ha sido eliminado de la lista de libros.")
        print (contenido)


archivo2="Llibres.txt"
eliminar_titulo(archivo2)