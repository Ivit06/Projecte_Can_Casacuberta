def anadir_libro():
    titulo = input("Introduce el título del libro: ")
    autor = input("Introduce el autor/a del libro: ")
    año = input("Introduce el año de publicación del libro: ")
    genero = input("Introduce el género del libro: ")
    isbn = input("Introduce el ISBN del libro: ")
    
    with open('../Llibres.txt', 'a') as file:
        file.write(f"{titulo}|{autor}|{año}|{genero}|{isbn}\n")

# Llamar a la función para añadir el libro
añadir_libro()
