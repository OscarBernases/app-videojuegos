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
    if not catalogo:
        return None
        
    mas_antiguo = None
    
    for juego in catalogo.values():
        if mas_antiguo is None or juego["anio"] < mas_antiguo["anio"]:
            mas_antiguo = juego
            
    return mas_antiguo["titulo"]


def videojuego_mas_reciente(catalogo):
    if not catalogo:
        return None
        
    mas_reciente = None
    
    for juego in catalogo.values():
        if mas_reciente is None or juego["anio"] > mas_reciente["anio"]:
            mas_reciente = juego
            
    return mas_reciente["titulo"]

def normalizar(texto):
    # Devuelve el texto en minúsculas y sin espacios sobrantes (también entre palabras).
    return " ".join(texto.lower().split())


def buscar_titulo_exacto(catalogo, titulo):
    # Devuelve el videojuego con ese título exacto, o None si no existe.
    titulo = normalizar(titulo)

    for juego in catalogo.values():
        if normalizar(juego["titulo"]) == titulo:
            return juego

    return None


def buscar_por_titulo_parcial(catalogo, texto):
    # Devuelve la lista de videojuegos cuyo título contiene el texto.
    texto = normalizar(texto)
    resultados = []

    if not texto:
        return resultados

    for juego in catalogo.values():
        if texto in normalizar(juego["titulo"]):
            resultados.append(juego)

    return resultados


def filtrar_por_genero(catalogo, genero):
    # Devuelve la lista de videojuegos que pertenecen a ese género.
    genero = normalizar(genero)
    resultados = []

    if not genero:
        return resultados

    for juego in catalogo.values():
        generos_juego = {normalizar(g) for g in juego["generos"]}
        if genero in generos_juego:
            resultados.append(juego)

    return resultados


def filtrar_por_rango_anios(catalogo, anio_min, anio_max):
    # Devuelve los videojuegos lanzados entre anio_min y anio_max (ambos incluidos).
    resultados = []

    for juego in catalogo.values():
        if anio_min <= juego["anio"] <= anio_max:
            resultados.append(juego)

    return resultados

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