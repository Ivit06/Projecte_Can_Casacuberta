def mostrar_todo (archivo):
    try:
        with open(archivo, 'r') as a:
            contenido = a.readlines()
            for linea in contenido:
                    print(linea)
    except FileNotFoundError:
        print("El archivo 'archivo.txt' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    else:
        a.close()

archivo2="Llibres.txt"
mostrar_todo(archivo2)