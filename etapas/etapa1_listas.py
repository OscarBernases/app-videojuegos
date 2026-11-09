def crear_lista():
    global videojuegos
    videojuegos = ["Grand Theft Auto V", "Call of Duty", "Valorant", "Fortnite ", "Minecraft"]

def visualizar_lista():
    print("Listado de videojuegos favoritos:")
    for juego in videojuegos:
        print(juego)

def agregar_videojuego(videojuego):
    videojuegos.append(videojuego)
    print(f"Se ha agregado el videojuego {videojuego} a la lista.")

def insertar_videojuego(posicion, videojuego):
    videojuegos.insert(posicion, videojuego)
    print(f"Se ha insertado el videojuego {videojuego} en la posición {posicion}.")

def eliminar_videojuego(videojuego):
    if videojuego in videojuegos:
        videojuegos.remove(videojuego)
        print(f"Se ha eliminado el videojuego {videojuego} de la lista.")
    else:
        print(f"El videojuego {videojuego} no esta en la lista.")

def ordenar_videojuegos():
    videojuegos.sort()

def visualizar_videojuegos_numerados():
    print("Listado de videojuegos numerados:")
    for indice, juego in enumerate(videojuegos , start=0):
        print(f"{indice}. {juego}")

def visualizar_videojuegos_ordenados():
    ordenar_videojuegos()
    print("Listado de videojuegos ordenados alfabéticamente:")
    for juego in videojuegos:
        print(juego)

def visualizar_menu():
    while True:
        print("\nMENÚ:")
        print("1. Visualizar lista de videojuegos")
        print("2. Agregar un videojuego")
        print("3. Insertar un videojuego en una posición determinada")
        print("4. Eliminar un videojuego")
        print("5. Mostrar videojuegos numerados")
        print("6. Mostrar videojuegos ordenados alfabéticamente")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ")

        match opcion:
            case "1":
                visualizar_lista()
            case "2":
                videojuego = input("Ingrese el título del videojuego a agregar: ")
                agregar_videojuego(videojuego)
            case "3":
                posicion = int(input("Ingrese la posición donde desea insertar el videojuego: "))
                videojuego = input("Ingrese el título del videojuego a insertar: ")
                insertar_videojuego(posicion, videojuego)
            case "4":
                videojuego = input("Ingrese el título del videojuego a eliminar: ")
                eliminar_videojuego(videojuego)
            case "5":
                visualizar_videojuegos_numerados()
            case "6":
                visualizar_videojuegos_ordenados()
            case "7":
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")

def main():
    crear_lista()
    visualizar_menu()

main()