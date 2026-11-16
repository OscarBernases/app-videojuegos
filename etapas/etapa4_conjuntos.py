def normalizar(texto):
    """Quita espacios y pasa a minúsculas para evitar duplicados como 'Rol' y 'rol'."""
    return texto.strip().lower()


def mostrar(titulo, conjunto):
    """Muestra un conjunto ordenado alfabéticamente (los sets no tienen orden)."""
    print(f"{titulo}: {', '.join(sorted(conjunto)) if conjunto else '(vacío)'}")


# 1. Crear el conjunto con los géneros de mi colección
#    (el duplicado "acción" se ignora automáticamente)
coleccion = {"acción", "aventura", "rpg", "estrategia", "deportes", "acción"}

# 2. Mostrar los géneros sin duplicados
mostrar("Géneros de mi colección", coleccion)

# 3. Añadir un nuevo género
nuevo = normalizar(input("\nEscribe un género para AÑADIR: "))
if nuevo:
    if nuevo in coleccion:
        print(f'"{nuevo}" ya estaba en el conjunto.')
    else:
        coleccion.add(nuevo)
        print(f'"{nuevo}" añadido.')
mostrar("Colección actualizada", coleccion)

# 4. Eliminar un género
borrar = normalizar(input("\nEscribe un género para ELIMINAR: "))
if borrar:
    if borrar in coleccion:
        coleccion.remove(borrar)
        print(f'"{borrar}" eliminado.')
    else:
        print(f'"{borrar}" no estaba en el conjunto.')
mostrar("Colección actualizada", coleccion)

# 5. Comprobar si un género pertenece al conjunto
buscar = normalizar(input("\nEscribe un género para COMPROBAR si está en tu colección: "))
if buscar:
    if buscar in coleccion:
        print(f'Sí, "{buscar}" está en tu colección.')
    else:
        print(f'No, "{buscar}" no está en tu colección.')

# 6. Conjunto con los géneros favoritos de otra persona
favoritos = {"rpg", "terror", "aventura", "carreras"}
print()
mostrar("Favoritos de la otra persona", favoritos)

# 7. Operaciones entre conjuntos
union = coleccion | favoritos             # también: coleccion.union(favoritos)
interseccion = coleccion & favoritos      # también: coleccion.intersection(favoritos)
diferencia = coleccion - favoritos        # también: coleccion.difference(favoritos)

print()
mostrar("Unión (todos los géneros)", union)
mostrar("Intersección (géneros comunes)", interseccion)
mostrar("Diferencia (míos que no están en sus favoritos)", diferencia)