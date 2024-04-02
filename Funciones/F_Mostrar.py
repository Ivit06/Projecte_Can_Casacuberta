def mostrar_libro (archivo):
    try:
        dato = input("Introduce el Títol o Autor/a o Any de publicació o Genere o ISBN del libro/s que quieres mostrar: ") #Si pones un genero hay que tener cuidado porque borra todos los de ese genero
        with open(archivo, 'r') as a:
            contenido = a.readlines()
            for linea in contenido:
                if dato in linea:
                    print(linea)
    except FileNotFoundError:
        print("El archivo 'archivo.txt' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    else:
        a.close()

archivo2="Llibres.txt"
mostrar_libro(archivo2)