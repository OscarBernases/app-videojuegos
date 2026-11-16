coleccion = {"acción", "aventura", "rpg", "estrategia", "deportes", "acción"}
print("Géneros de mi colección:", coleccion)

genero = input("Escribe un género para añadir: ").strip().lower()
if genero in coleccion:
    print("Ese género ya está")
else:
    coleccion.add(genero)
    print("Género añadido")
print("Colección:", coleccion)

genero = input("Escribe un género para eliminar: ").strip().lower()
if genero in coleccion:
    coleccion.remove(genero)
    print("Género eliminado")
else:
    print("Ese género no está en la colección")
print("Colección:", coleccion)

genero = input("Escribe un género para comprobar: ").strip().lower()
if genero in coleccion:
    print("Sí está en la colección")
else:
    print("No está en la colección")

favoritos = {"rpg", "terror", "aventura", "carreras"}
print("Favoritos de la otra persona:", favoritos)

print("Unión:", coleccion.union(favoritos))
print("Intersección:", coleccion.intersection(favoritos))
print("Diferencia:", coleccion.difference(favoritos))