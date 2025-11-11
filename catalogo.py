import json
import os

ARCHIVO = "biblioteca.json"

def guardar_datos(datos):
    """Guarda los datos de la biblioteca en un archivo JSON."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print("Datos guardados correctamente.")

def cargar_datos():
    """Carga los datos desde el archivo JSON si existe, o devuelve lista vacía."""
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
        print("Datos cargados correctamente.")
        return datos
    else:
        print("No hay datos previos. Se creará una nueva biblioteca.")
        return {"libros": []}
