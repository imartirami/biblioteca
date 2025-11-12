import json
import os
from pathlib import Path

ARCHIVO = "biblioteca.json"

def guardar_datos(datos):
    """Guarda los datos de la biblioteca en un archivo JSON."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print("Datos guardados correctamente.")

def crea_archivo_json():
    """Crea un archivo JSON con una lista inicial de libros."""
    libros = [
        {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "disponible": True},
        {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "disponible": True},
        {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón", "disponible": True},
        {"titulo": "1984", "autor": "George Orwell", "disponible": True},
        {"titulo": "El Nombre de la Rosa", "autor": "Umberto Eco", "disponible": True},
        {"titulo": "Orgullo y Prejuicio", "autor": "Jane Austen", "disponible": True},
        {"titulo": "Matar a un Ruiseñor", "autor": "Harper Lee", "disponible": True},
        {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "disponible": True},
        {"titulo": "Crimen y Castigo", "autor": "Fiódor Dostoyevski", "disponible": True},
        {"titulo": "Ulises", "autor": "James Joyce", "disponible": True},
        {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "disponible": True},
        {"titulo": "El Gran Gatsby", "autor": "F. Scott Fitzgerald", "disponible": True},
        {"titulo": "La Metamorfosis", "autor": "Franz Kafka", "disponible": True},
        {"titulo": "El Señor de los Anillos", "autor": "J.R.R. Tolkien", "disponible": True},
        {"titulo": "En Busca del Tiempo Perdido", "autor": "Marcel Proust", "disponible": True},
        {"titulo": "La Iliada", "autor": "Homero", "disponible": True},
        {"titulo": "La Odisea", "autor": "Homero", "disponible": True},
        {"titulo": "Rayuela", "autor": "Julio Cortázar", "disponible": True},
        {"titulo": "Pedro Páramo", "autor": "Juan Rulfo", "disponible": True},
        {"titulo": "El Amor en los Tiempos del Cólera", "autor": "Gabriel García Márquez", "disponible": True},
        {"titulo": "El Retrato de Dorian Gray", "autor": "Oscar Wilde", "disponible": True},
        {"titulo": "Los Miserables", "autor": "Victor Hugo", "disponible": True}
    ]
    ruta = Path('biblioteca.json')
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with ruta.open('w', encoding='utf-8') as f:
        json.dump({"libros": libros}, f, ensure_ascii=False,indent=2)
    print('catalogo cargado')
    return {"libros": libros}

def cargar_datos():
    """Carga los datos desde el archivo JSON si existe, o devuelve lista vacía."""
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
        print("Datos cargados correctamente.")
        return datos
    else:
        print("Archivo no encontrado. Creando un nuevo archivo con datos iniciales.")
        return crea_archivo_json()