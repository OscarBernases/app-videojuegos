def formatear_videojuego(juego):
    titulo = juego[0]
    anio = juego[1]
    genero = juego[2]
    return f"{titulo} ({anio}) - {genero}"


def normalizar_texto(texto):
    # minúsculas y sin espacios sobrantes (también entre palabras)
    return " ".join(texto.lower().split())


def buscar_por_titulo(videojuegos, texto):
    # devuelve los juegos cuyo título contiene el texto (búsqueda parcial)
    texto = normalizar_texto(texto)
    resultados = []
    for juego in videojuegos:
        if texto in normalizar_texto(juego[0]):
            resultados.append(juego)
    return resultados


def mostrar_resultados(resultados):
    if not resultados:
        print("No se han encontrado coincidencias.")
        return
    print("Videojuegos encontrados:")
    for juego in resultados:
        print(formatear_videojuego(juego))


def main():
    videojuegos = [
        ("The Legend of Zelda", 1986, "Aventura"),
        ("Grand Theft Auto V", 2013, "Acción"),
        ("Minecraft", 2011, "Sandbox"),
        ("Valorant", 2020, "Shooter"),
        ("Fortnite", 2017, "Battle Royale")
    ]

    texto = input("Introduce el título a buscar: ")
    if not normalizar_texto(texto):
        print("Debes escribir algo para buscar.")
        return

    resultados = buscar_por_titulo(videojuegos, texto)
    mostrar_resultados(resultados)


# Arrancamos programa
main()