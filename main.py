from gestor import consola

catalogo_videojuegos = {
    "Grand Theft Auto V": {
        "titulo": "Grand Theft Auto V",
        "anio": 2013,
        "generos": {"Acción", "Aventura"},
    },
    "Call of Duty": {
        "titulo": "Call of Duty",
        "anio": 2003,
        "generos": {"Shooter", "Acción"},
    },
    "Valorant": {
        "titulo": "Valorant",
        "anio": 2020,
        "generos": {"Shooter", "Multijugador"},
    },
    "Fortnite": {
        "titulo": "Fortnite",
        "anio": 2017,
        "generos": {"Battle Royale", "Multijugador"},
    },
    "Minecraft": {
        "titulo": "Minecraft",
        "anio": 2011,
        "generos": {"Sandbox", "Aventura"},
    },
}

consola.ejecutar_menu(catalogo_videojuegos)
