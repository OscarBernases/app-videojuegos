# Normalizamos los titulos
def normalizar_titulo(titulo):
    titulo_limpio = titulo.strip().lower().split()
    # concatenar los titulos con un espacio en blanco entre palabras
    return " ".join(titulo_limpio) 

# Validamos
def validar_datos_juego(titulo,anio,generos):
    tit = normalizar_titulo(titulo)
    if (tit == ""):
        return False
    if (type(anio) is not int or anio <= 0):
        return False
    return len(generos) > 0

# 1. CREAR 
def agregar_videojuego(catalogo, titulo, anio, generos):
    if not validar_datos_juego(titulo, anio, generos):
        return False
    
    txt = normalizar_titulo(titulo)

    if txt in catalogo:
        return False  # No permitir titulos duplicados
    
    catalogo[txt] = {
        "titulo": titulo.strip(),
        "anio": anio,
        "generos": set(generos)
    }

    return True

# 2. LEER 
def obtener_videojuego(catalogo, titulo):
    clave = normalizar_titulo(titulo)

    return catalogo.get(clave, None)

# 3. ACTUALIZAR 
def actualizar_videojuego(catalogo, titulo_actual, nuevo_titulo, nuevo_anio, nuevos_generos):
    clave_actual = normalizar_titulo(titulo_actual)

    if clave_actual not in catalogo:
        return False
    
    if not validar_datos_juego(nuevo_titulo, nuevo_anio, nuevos_generos):
        return False
    
    nueva_clave = normalizar_titulo(nuevo_titulo)

    if nueva_clave != clave_actual and nueva_clave in catalogo:
        return False  # El nuevo titulo ya existe en otro juego
    
    del catalogo[clave_actual]

    catalogo[nueva_clave] = {
        "titulo": nuevo_titulo.strip(),
        "anio": nuevo_anio,
        "generos": set(nuevos_generos)
    }

    return True

# 4. ELIMINAR 
def eliminar_videojuego(catalogo, titulo):
    clave = normalizar_titulo(titulo)

    if clave not in catalogo:
        return False
    
    del catalogo[clave]
    
    return True