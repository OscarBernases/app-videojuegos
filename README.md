# Gestor de videojuegos

Práctica Gestión de Videojuegos (Grupo 2).

## Estructura del proyecto

```
app-videojuegos/
├── main.py
├── gestor/
│   ├── __init__.py
│   ├── catalogo.py
│   ├── consultas.py
│   └── consola.py
├── etapas/
│   ├── etapa1_listas.py
│   ├── etapa2_tuplas.py
│   ├── etapa3_cadenas.py
│   └── etapa4_conjuntos.py
├── README.md
└── .gitignore
```

## Quién hace cada parte del proyecto

### Etapas

| Etapa | Archivo | Responsable |
|---|---|---|
| 1. Listas | `etapas/etapa1_listas.py` | Óscar |
| 2. Tuplas | `etapas/etapa2_tuplas.py` | Mario |
| 3. Cadenas | `etapas/etapa3_cadenas.py` | Alfonso |
| 4. Conjuntos | `etapas/etapa4_conjuntos.py` | Kenneth |

### Proyecto

| Archivo | Contenido | Responsable |
|---|---|---|
| `gestor/catalogo.py` | Operaciones CRUD, normalización y validación | Mario |
| `gestor/consultas.py` (parte de estadísticas) | Total, recuento por género, más antiguo y más reciente | Óscar |
| `gestor/consultas.py` (parte de búsquedas) | Por título parcial, por género y por rango de años | Alfonso |
| `gestor/consola.py` | Menú interactivo y validación de datos | Kenneth |
| `main.py` | Catálogo inicial con al menos cinco juegos y bucle principal | Óscar |

## Reparto de tareas

### Óscar
- Crear el repositorio en GitHub e invitar al resto del equipo.
- Etapa 1 (listas): `etapas/etapa1_listas.py`.
- Funciones de estadísticas en `gestor/consultas.py`: total de juegos, recuento por género, juego más antiguo y más reciente.
- Catálogo inicial con al menos cinco juegos y bucle principal de `main.py`.
- Configurar `.gitignore` y estructurar el `README.md` inicial.

### Mario
- Etapa 2 (tuplas): `etapas/etapa2_tuplas.py`.
- Módulo `gestor/catalogo.py` con las operaciones CRUD (crear, leer, actualizar y eliminar) sobre el diccionario de diccionarios.
- Normalización de títulos e identificadores, sin títulos duplicados ni listas de géneros vacías.

### Kenneth
- Etapa 4 (conjuntos): `etapas/etapa4_conjuntos.py`.
- Módulo `gestor/consola.py`: menú interactivo y solicitud y validación de datos.

### Alfonso
- Etapa 3 (cadenas): `etapas/etapa3_cadenas.py`.
- Funciones de búsqueda y filtrado en `gestor/consultas.py`: por título parcial, por género y por rango de años.
