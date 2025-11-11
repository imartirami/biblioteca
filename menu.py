from modelo import Biblioteca

def menu(biblioteca):
    while True:
        print("\n=== MENÚ DE BIBLIOTECA ===")
        print("1. Agregar libro")
        print("2. Mostrar todos los libros")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Buscar por autor")
        print("6. Mostrar libros prestados")
        print("7. Salir")

        opcion = input("Selecciona una opción (1-7): ")

        match opcion:
            case "1":
                titulo = input("Título del libro: ")
                autor = input("Autor del libro: ")
                biblioteca.agregar_libro(titulo, autor)
            case "2":
                biblioteca.mostrar_libros()
            case "3":
                titulo = input("Título del libro a prestar: ")
                biblioteca.prestar_libro(titulo)
            case "4":
                titulo = input("Título del libro a devolver: ")
                biblioteca.devolver_libro(titulo)
            case "5":
                autor = input("Autor a buscar: ")
                biblioteca.buscar_por_autor(autor)
            case "6":
                biblioteca.mostrar_prestados()
            case "7":
                print("Guardando datos y saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    # Crear la biblioteca (carga automática de datos existentes)
    biblioteca = Biblioteca()
    try:
        menu(biblioteca)
    finally:
        # Guardar siempre los datos al salir
        biblioteca._guardar()
        print("Datos guardados correctamente. ¡Hasta luego!")
