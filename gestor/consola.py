import catalogo
import consultas


def mostrar_menu():
    print()
    print("--- CATÁLOGO DE VIDEOJUEGOS ---")
    print("1. Añadir videojuego")
    print("2. Ver todos los videojuegos")
    print("3. Ver un videojuego por id")
    print("4. Actualizar videojuego")
    print("5. Eliminar videojuego")
    print("6. Buscar por título")
    print("7. Buscar por género")
    print("8. Buscar por rango de años")
    print("9. Estadísticas")
    print("0. Salir")


def pedir_numero(mensaje, minimo, maximo):
    while True:
        try:
            numero = int(input(mensaje))
            if numero >= minimo and numero <= maximo:
                return numero
            print(f"Tiene que estar entre {minimo} y {maximo}")
        except ValueError:
            print("Tienes que escribir un número")


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("No puede estar vacío")


def pedir_videojuego(lista):
    while True:
        id = pedir_numero("Id del videojuego: ", 1, 100000)
        videojuego = catalogo.leer_videojuego(lista, id)
        if videojuego is None:
            print("No existe ningún videojuego con ese id")
        else:
            return videojuego


def mostrar_videojuego(v):
    print(f"{v['id']} - {v['titulo']} ({v['genero']}, {v['anio']})")


def mostrar_lista(resultado):
    if len(resultado) == 0:
        print("No se ha encontrado ningún videojuego")
    else:
        for v in resultado:
            mostrar_videojuego(v)
        print("Total:", len(resultado))


def anadir(lista):
    titulo = pedir_texto("Título: ")
    genero = pedir_texto("Género: ")
    anio = pedir_numero("Año: ", 1950, 2030)
    nuevo = catalogo.crear_videojuego(lista, titulo, genero, anio)
    print("Videojuego añadido con id", nuevo["id"])


def actualizar(lista):
    v = pedir_videojuego(lista)
    print("Datos actuales:")
    mostrar_videojuego(v)
    titulo = pedir_texto("Nuevo título: ")
    genero = pedir_texto("Nuevo género: ")
    anio = pedir_numero("Nuevo año: ", 1950, 2030)
    catalogo.actualizar_videojuego(lista, v["id"], titulo, genero, anio)
    print("Videojuego actualizado")


def eliminar(lista):
    v = pedir_videojuego(lista)
    mostrar_videojuego(v)
    respuesta = input("¿Seguro que quieres eliminarlo? (s/n): ").lower()
    if respuesta == "s":
        catalogo.eliminar_videojuego(lista, v["id"])
        print("Videojuego eliminado")
    else:
        print("No se ha eliminado")


def buscar_anios(lista):
    while True:
        desde = pedir_numero("Desde el año: ", 1950, 2030)
        hasta = pedir_numero("Hasta el año: ", 1950, 2030)
        if desde <= hasta:
            break
        print("El primer año no puede ser mayor que el segundo")
    mostrar_lista(consultas.buscar_por_anios(lista, desde, hasta))


def estadisticas(lista):
    print("Número total de videojuegos:", consultas.total_videojuegos(lista))
    conteo = consultas.conteo_por_genero(lista)
    print("Videojuegos por género:")
    for genero in conteo:
        print(f"{genero}: {conteo[genero]}")


def ejecutar_menu(lista):
    while True:
        mostrar_menu()
        opcion = pedir_numero("Opción: ", 0, 9)

        if opcion == 1:
            anadir(lista)
        elif opcion == 2:
            mostrar_lista(catalogo.listar_videojuegos(lista))
        elif opcion == 3:
            mostrar_videojuego(pedir_videojuego(lista))
        elif opcion == 4:
            actualizar(lista)
        elif opcion == 5:
            eliminar(lista)
        elif opcion == 6:
            texto = pedir_texto("Texto a buscar en el título: ")
            mostrar_lista(consultas.buscar_por_titulo(lista, texto))
        elif opcion == 7:
            genero = pedir_texto("Género: ")
            mostrar_lista(consultas.buscar_por_genero(lista, genero))
        elif opcion == 8:
            buscar_anios(lista)
        elif opcion == 9:
            estadisticas(lista)
        elif opcion == 0:
            print("Fin del programa")
            break