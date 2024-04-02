def eliminar_titulo (archivo):
    try:
        dato = input("Introduce el Títol o Autor/a o Any de publicació o Genere o ISBN del libro/s que quieres eliminar: ") #Si pones un genero hay que tener cuidado porque borra todos los de ese genero
        with open(archivo, 'r') as a:
            contenido = a.readlines()
        with open(archivo, 'w') as a:
            for linea in contenido:
                if dato not in linea:
                    a.write(linea)
    except FileNotFoundError:
        print("El archivo 'archivo.txt' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    else:
        print(f"El libro con este dato {dato} ha sido eliminado de la lista de libros.")
        a.close()

archivo2="Llibres.txt"
eliminar_titulo(archivo2)