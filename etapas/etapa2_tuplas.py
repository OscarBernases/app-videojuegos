def formatear_videojuego(juego):
    titulo = juego[0]
    anio = juego[1]
    genero = juego[2]
    return f"{titulo} ({anio}) - {genero}"

def main():
    # 1 lista con los 5 videojuegos
    videojuegos = [
        ("The Legend of Zelda", 1986, "Aventura"),
        ("Grand Theft Auto V", 2013, "Acción"),
        ("Minecraft", 2011, "Sandbox"),
        ("Valorant", 2020, "Shooter"),
        ("Fortnite", 2017, "Battle Royale")
    ]

    print("Lista de videojuegos: ")
    for juego in videojuegos:
        texto = formatear_videojuego(juego)
        print(texto)

# Arrancamos programa
main()

