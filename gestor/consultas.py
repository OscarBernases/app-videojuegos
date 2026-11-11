def total_videojuegos(catalogo):
    #Calcula el número total de videojuegos en el catálogo.
    return len(catalogo)

def contar_por_genero(catalogo):
    #Devuelve un diccionario {genero: cantidad de videojuegos con ese genero}.
    #Si un videojuego tiene varios géneros, se cuenta en todos ellos.

    conteo_generos = {}

    for juego in catalogo.values(): # Por cada juego en el catálogo
        for genero in juego["generos"]: # Por cada genero del juego
            conteo_generos[genero] = conteo_generos.get(genero, 0) + 1

    return conteo_generos


def videojuego_mas_antiguo(catalogo):
    # Devuelve el videojuego con menor año, o None si el catálogo está vacío.
    if not catalogo:
        return None
    return min(catalogo.values(), key=lambda juego: juego["anio"])


def videojuego_mas_reciente(catalogo):
    # Devuelve el videojuego con mayor año, o None si el catálogo está vacío.
    if not catalogo:
        return None
    return max(catalogo.values(), key=lambda juego: juego["anio"])


def test():
    # Función para testear pruebas rápidas de las funciones de estadísticas.
    catalogo = {
        "Grand Theft Auto V": {"titulo": "Grand Theft Auto V", "anio": 2013, "generos": {"Acción", "Aventura"}},
        "Call of Duty": {"titulo": "Call of Duty", "anio": 2003, "generos": {"Shooter", "Acción"}},
        "Valorant": {"titulo": "Valorant", "anio": 2020, "generos": {"Shooter", "Multijugador"}},
        "Fortnite": {"titulo": "Fortnite", "anio": 2017, "generos": {"Battle Royale", "Multijugador"}},
        "Minecraft": {"titulo": "Minecraft", "anio": 2011, "generos": {"Sandbox", "Aventura"}},
    }

    catalogo_vacio = {}

    print("Total de videojuegos:", total_videojuegos(catalogo))
    print("Conteo por género:", contar_por_genero(catalogo))
    print("Videojuego más antiguo:", videojuego_mas_antiguo(catalogo))
    print("Videojuego más reciente:", videojuego_mas_reciente(catalogo))

    print("Total de videojuegos:", total_videojuegos(catalogo_vacio))
    print("Conteo por género:", contar_por_genero(catalogo_vacio))
    print("Videojuego más antiguo:", videojuego_mas_antiguo(catalogo_vacio))
    print("Videojuego más reciente:", videojuego_mas_reciente(catalogo_vacio))

test()