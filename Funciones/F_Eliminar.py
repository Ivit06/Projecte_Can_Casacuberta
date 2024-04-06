def eliminar_titulo (archivo):
    try:
        dato = input("Introduce el ISBN del libro que quieres eliminar: ") 
        tamaño = len(dato)
        if tamaño == 17:
            with open(archivo, 'r') as a:
                contenido = a.readlines()
            with open(archivo, 'w') as a:
                for linea in contenido:
                    if dato not in linea:
                        a.write(linea)
            print(f"El libro con este dato {dato} ha sido eliminado de la lista de libros.")
            a.close()
        else:
            print ("El número de IBAN que has introducido no es correcto. Asegurese que haya los 17 carácteres que pertocan.")
            eliminar_titulo(archivo)
    except FileNotFoundError:
        print("El archivo 'archivo.txt' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")