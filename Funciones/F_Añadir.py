def anadir_libro():
    try:
        titulo = input("Introduce el título del libro: ")
        autor = input("Introduce el autor/a del libro: ")
        año = input("Introduce el año de publicación del libro: ")
        genero = input("Introduce el género del libro: ")
        isbn = input("Introduce el ISBN del libro: ")
    except TypeError:
        print ("El parámetro es incorrecto")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    else:
        with open('../Llibres.txt', 'a') as file:
            file.write(f"{titulo}|{autor}|{año}|{genero}|{isbn}\n")
        file.close()
        print("Se ha añadido el libro")
