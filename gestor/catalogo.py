# Normalizamos los titulos
def normalizarTitulo(titulo):
    tituloLimpio = titulo.strip().lower().split()
    # concatenar los titulos con un espacio en blanco entre palabras
    return " ".join(tituloLimpio) 

# Validamos
def validarDatosJuego(titulo,anio,generos):
    tit = normalizarTitulo(titulo)
    if (tit == ""):
        return False
    if (type(anio) is not int or anio <= 0):
        return False
    return len(generos) > 0

# 1. CREAR 
def agregarVideojuego(catalogo, titulo, anio, generos):
    if not validarDatosJuego(titulo, anio, generos):
        return False
    
    txt = normalizarTitulo(titulo)

    if txt in catalogo:
        return False  # No permitir titulos duplicados
    
    catalogo[txt] = {
        "titulo": titulo.strip(),
        "anio": anio,
        "generos": set(generos)
    }

    return True

# 2. LEER 
def obtenerVideojuego(catalogo, titulo):
    clave = normalizarTitulo(titulo)

    return catalogo.get(clave, None)

# 3. ACTUALIZAR 
def actualizarVideojuego(catalogo, tituloActual, nuevoTitulo, nuevoAnio, nuevosGeneros):
    claveActual = normalizarTitulo(tituloActual)

    if claveActual not in catalogo:
        return False
    
    if not validarDatosJuego(nuevoTitulo, nuevoAnio, nuevosGeneros):
        return False
    
    nuevaClave = normalizarTitulo(nuevoTitulo)

    if nuevaClave != claveActual and nuevaClave in catalogo:
        return False  # El nuevo titulo ya existe en otro juego
    
    del catalogo[claveActual]

    catalogo[nuevaClave] = {
        "titulo": nuevoTitulo.strip(),
        "anio": nuevoAnio,
        "generos": set(nuevosGeneros)
    }

    return True

# 4. ELIMINAR 
def eliminarVideojuego(catalogo, titulo):
    clave = normalizarTitulo(titulo)

    if clave not in catalogo:
        return False
    
    del catalogo[clave]
    
    return True