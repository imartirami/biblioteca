class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor):
        self.libros.append({"titulo": titulo, "autor": autor, "disponible": True})
        print(f" Libro '{titulo}' agregado correctamente.")

    def mostrar_libros(self):
        if not self.libros:
            print(" No hay libros en la biblioteca.")
        else:
            print("\n Lista de libros:")
            for libro in self.libros:
                estado = "Disponible" if libro["disponible"] else "Prestado"
                print(f" - {libro['titulo']} ({libro['autor']}) - {estado}")

    def buscar_por_autor(self, autor):
        encontrados = [l for l in self.libros if l["autor"].lower() == autor.lower()]
        if encontrados:
            print("\n🔍 Libros encontrados:")
            for libro in encontrados:
                estado = "Disponible" if libro["disponible"] else "Prestado"
                print(f" - {libro['titulo']} ({estado})")
        else:
            print(" No se encontraron libros de ese autor.")

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro["titulo"].lower() == titulo.lower():
                if libro["disponible"]:
                    libro["disponible"] = False
                    print(f" Libro '{titulo}' prestado con éxito.")
                    return
                else:
                    print(" Ese libro ya está prestado.")
                    return
        print(" Libro no encontrado.")

    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro["titulo"].lower() == titulo.lower():
                if not libro["disponible"]:
                    libro["disponible"] = True
                    print(f"🔁 Libro '{titulo}' devuelto correctamente.")
                    return
                else:
                    print(" Ese libro no estaba prestado.")
                    return
        print(" Libro no encontrado.")

    def menu(self):
        while True:
            print("\n=== Sistema de Gestión de Biblioteca ===")
            print("1. Agregar libro")
            print("2. Mostrar libros")
            print("3. Buscar por autor")
            print("4. Prestar libro")
            print("5. Devolver libro")
            print("6. Salir")
            opcion = input("Selecciona una opción: ")

            match opcion:
                case "1":
                    titulo = input("Título del libro: ")
                    autor = input("Autor del libro: ")
                    self.agregar_libro(titulo, autor)
                case "2":
                    self.mostrar_libros()
                case "3":
                    autor = input("Nombre del autor: ")
                    self.buscar_por_autor(autor)
                case "4":
                    titulo = input("Título del libro a prestar: ")
                    self.prestar_libro(titulo)
                case "5":
                    titulo = input("Título del libro a devolver: ")
                    self.devolver_libro(titulo)
                case "6":
                    print(" Saliendo del sistema...")
                    break
                case _:
                    print(" Opción no válida. Intenta de nuevo.")


# Ejecución principal
if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.menu()
