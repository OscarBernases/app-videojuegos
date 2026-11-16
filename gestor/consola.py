from . import catalogo as cat
from . import consultas as cons


def mostrar_menu():
    print()
    print("CATÁLOGO DE VIDEOJUEGOS")
    print()
    print("1. Añadir videojuego")
    print("2. Ver todos los videojuegos")
    print("3. Ver un videojuego por título")
    print("4. Actualizar videojuego")
    print("5. Eliminar videojuego")
    print("6. Buscar por título (parcial)")
    print("7. Buscar por género")
    print("8. Buscar por rango de años")
    print("9. Estadísticas")
    print("0. Salir")


def pedir_numero(mensaje, minimo, maximo):
    while True:
        try:
            numero = int(input(mensaje))
            if minimo <= numero <= maximo:
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


def mostrar_videojuego(v):
    # v es un diccionario con la estructura interna del juego
    generos_str = ", ".join(v["generos"])
    print(f"- {v['titulo']} ({generos_str}, {v['anio']})")


def mostrar_lista(resultado):
    if len(resultado) == 0:
        print("No se ha encontrado ningún videojuego")
    else:
        for v in resultado:
            mostrar_videojuego(v)
        print("Total:", len(resultado))


def anadir(catalogo):
    titulo = pedir_texto("Título: ")
    genero_str = pedir_texto("Género(s) separados por comas: ")
    # Convertimos los géneros introducidos en una lista quitando espacios
    generos = [g.strip() for g in genero_str.split(",")]
    anio = pedir_numero("Año: ", 1950, 2030)

    exito = cat.agregar_videojuego(catalogo, titulo, anio, generos)
    if exito:
        print("Videojuego añadido correctamente.")
    else:
        print("Error: El videojuego ya existe o los datos no son válidos.")


def actualizar(catalogo):
    titulo_actual = pedir_texto("Título del videojuego a actualizar: ")
    v = cat.obtener_videojuego(catalogo, titulo_actual)

    if v is None:
        print("No existe ningún videojuego con ese título.")
        return

    print("Datos actuales:")
    mostrar_videojuego(v)

    nuevo_titulo = pedir_texto("Nuevo título: ")
    genero_str = pedir_texto("Nuevos género(s) separados por comas: ")
    nuevos_generos = [g.strip() for g in genero_str.split(",")]
    nuevo_anio = pedir_numero("Nuevo año: ", 1950, 2030)

    exito = cat.actualizar_videojuego(
        catalogo, titulo_actual, nuevo_titulo, nuevo_anio, nuevos_generos
    )
    if exito:
        print("Videojuego actualizado correctamente.")
    else:
        print("Error al actualizar (es posible que el nuevo título ya exista).")


def eliminar(catalogo):
    titulo = pedir_texto("Título del videojuego a eliminar: ")
    v = cat.obtener_videojuego(catalogo, titulo)

    if v is None:
        print("No existe ningún videojuego con ese título.")
        return

    mostrar_videojuego(v)
    respuesta = input("¿Seguro que quieres eliminarlo? (s/n): ").lower()
    if respuesta == "s":
        cat.eliminar_videojuego(catalogo, titulo)
        print("Videojuego eliminado.")
    else:
        print("No se ha eliminado.")


def buscar_anios(catalogo):
    while True:
        desde = pedir_numero("Desde el año: ", 1950, 2030)
        hasta = pedir_numero("Hasta el año: ", 1950, 2030)
        if desde <= hasta:
            break
        print("El primer año no puede ser mayor que el segundo.")
    mostrar_lista(cons.filtrar_por_rango_anios(catalogo, desde, hasta))


def estadisticas(catalogo):
    print("Número total de videojuegos:", cons.total_videojuegos(catalogo))
    conteo = cons.contar_por_genero(catalogo)
    print("Videojuegos por género:")
    for genero, cantidad in conteo.items():
        print(f"  - {genero}: {cantidad}")
    print("Videojuego más antiguo:", cons.videojuego_mas_antiguo(catalogo))
    print("Videojuego más reciente:", cons.videojuego_mas_reciente(catalogo))


def ejecutar_menu(catalogo):
    while True:
        mostrar_menu()
        opcion = pedir_numero("Introduce el número de tu opción: ", 0, 9)

        match opcion:
            case 1:
                anadir(catalogo)
            case 2:
                mostrar_lista(list(catalogo.values()))
            case 3:
                titulo = pedir_texto("Título del videojuego: ")
                v = cat.obtener_videojuego(catalogo, titulo)
                if v:
                    mostrar_videojuego(v)
                else:
                    print("No se ha encontrado el videojuego.")
            case 4:
                actualizar(catalogo)
            case 5:
                eliminar(catalogo)
            case 6:
                texto = pedir_texto("Texto a buscar en el título: ")
                mostrar_lista(cons.buscar_por_titulo_parcial(catalogo, texto))
            case 7:
                genero = pedir_texto("Género: ")
                mostrar_lista(cons.filtrar_por_genero(catalogo, genero))
            case 8:
                buscar_anios(catalogo)
            case 9:
                estadisticas(catalogo)
            case _:
                print("Fin del programa")
                break
