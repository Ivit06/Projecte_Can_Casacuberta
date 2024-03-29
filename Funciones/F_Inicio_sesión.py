import hashlib

def leer_usuarios_contrasenas(archivo):
    usuarios_contrasenas = {}

    try:
        with open(archivo, 'r') as file:
            for linea in file:
                usuario, contrasena_cifrada = linea.strip().split('|')
                usuarios_contrasenas[usuario] = contrasena_cifrada
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no se encontró.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

    return usuarios_contrasenas

def iniciar_sesion(usuarios):
    intentos = 3

    try:
        while intentos > 0:
            usuario = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            contrasena_cifrada = hashlib.md5(contrasena.encode()).hexdigest()

            if usuario in usuarios and usuarios[usuario] == contrasena_cifrada:
                print("Inicio de sesión exitoso.")
                return True
            else:
                print("Nombre de usuario o contraseña incorrectos.")
                intentos -= 1
                print(f"Le quedan {intentos} intentos.")

        print("Ha excedido el número de intentos permitidos. Inténtelo más tarde.")
        return False

    except Exception as e:
        print(f"Error durante el inicio de sesión: {e}")
        return False

archivo = "Usuarios.txt"
usuarios = leer_usuarios_contrasenas(archivo)

if usuarios:
    inicio_correcto = iniciar_sesion(usuarios)
    if not inicio_correcto:
        print("Cierre del programa.")
else:
    print("No se pueden iniciar sesiones porque no hay usuarios registrados.")
