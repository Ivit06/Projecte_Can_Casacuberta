#Des de este simplente llamaremos a las funciones que estan en la carpeta /Funciones/F_loquesea. Allí pondremos todo el código.
#Vamos a usar archivo="Usuaris.txt" y archivo2="Llibres.txt".

from Funciones.F_Inicio_sesión import leer_usuarios_contrasenas, iniciar_sesion
from Funciones.F_Mostrar import mostrar_libro
from Funciones.F_Mostrar_todos import mostrar_todo
from Funciones.F_Eliminar import eliminar_titulo
from Funciones.F_Editar import editar_libro, solicitar_isbn
from Funciones.F_Añadir import anadir_libro
import os

archivo = "Usuaris.txt"
archivo2 = "Llibres.txt"

usuarios = leer_usuarios_contrasenas(archivo)
if usuarios:
    inicio_correcto = iniciar_sesion(usuarios)
    if not inicio_correcto:
        print("Cerrando el programa")
        os._exit(0)
else:
    print("No se pueden iniciar sesiones porque no hay usuarios registrados.")

def acc():
    try:
        acción = input("Que acción desea realizar: \n   1.Añadir libro. \n   2.Mostrar todos los libros. \n   3.Mostrar un libro. \n   4.Eliminar libro. \n   5.Editar libro. \n")
        acción = int(acción)
        if acción==1:
            anadir_libro(archivo2)
        if acción==2:
            mostrar_todo(archivo2)
        if acción==3:
            mostrar_libro(archivo2)
        if acción==4:
            eliminar_titulo(archivo2)
        if acción==5:
            isbn_a_editar = solicitar_isbn()
            if isbn_a_editar:
                nuevo_contenido = input("Introduzca el nuevo contenido del libro en el formato Título|Autor|Año|Género|ISBN: ")
                editar_libro(archivo, isbn_a_editar, nuevo_contenido)
            else:
                print("Saliendo del programa.")
                os._exit(0)
        if acción==0 or acción>5:
            print ("Esta acción no se puede realizar. \nIntentelo de nuevo: ")
            acc()

    except Exception as e:
        print(f"Ocurrió un error: {e}")

acc()

def c():
    conti=input("Desea continuar realizando acciónes: Si/No\n")
    if conti == "Si":
        acc()
    if conti =="No":
        print("Hasta otra. \nPrograma finalizado.")
        os._exit(0)
    if conti !="Si" "No":
        print("Introduzca un valor válido")
        c()

c()

# Las dos últimas funciones las hemos hecho en el código principal ya que no se piden en el enunciado pero nos parecia interesante hacerlas.