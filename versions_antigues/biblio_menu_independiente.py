class Biblioteca:
    def __init__(self):
        self.total_libros = 0
        self.total_libros_prestados = 0
        self.libros = []
        self.libros_prestados = []
    
    def agregar_libro(self, titulo, autor):
        for libro in self.libros:
            if libro["titulo"].lower() == titulo.lower():
                print(f'El libro "{titulo}" ya existe en la biblioteca.')
                return
        self.libros.append({"titulo": titulo, "autor": autor, "disponible": True})
        self.total_libros += 1
        print(f'Título: "{titulo}" agregado correctamente.')
        print(f'Total de libros: {self.total_libros}')

    def mostrar_libros(self):
        if not self.libros:
            print('La lista está vacía.')
        else:
            print(f'\nHay {self.total_libros} libros en la biblioteca:')
            for libro in self.libros:
                estado = "Disponible" if libro["disponible"] else "Prestado"
                print(f' - "{libro["titulo"]}" de {libro["autor"]} [{estado}]')

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro["titulo"].lower() == titulo.lower():
                if not libro["disponible"]:
                    print(f'El libro "{titulo}" ya está prestado.')
                    return
                libro["disponible"] = False
                self.libros_prestados.append(libro)
                self.total_libros_prestados += 1
                print(f'Has retirado el libro "{titulo}".')
                print(f'La biblioteca lleva {self.total_libros_prestados} préstamos en total.')
                return
        print("Libro no encontrado.")

    def devolver_libro(self, titulo):
        for libro in self.libros_prestados:
            if libro["titulo"].lower() == titulo.lower():
                libro["disponible"] = True
                self.libros_prestados.remove(libro)
                print(f'Has devuelto el libro "{titulo}".')
                print(f'Quedan {len(self.libros_prestados)} libros prestados actualmente.')
                return
        print("No se encontró el libro en la lista de préstamos.")

    def buscar_por_autor(self, autor):
        encontrados = [libro for libro in self.libros if libro["autor"].lower() == autor.lower()]
        if encontrados:
            print("\nLibros encontrados:")
            for libro in encontrados:
                estado = "Disponible" if libro["disponible"] else "Prestado"
                print(f" - {libro['titulo']} ({estado})")
        else:
            print("No se encontraron libros de ese autor.")

    def mostrar_prestados(self):
        if not self.libros_prestados:
            print("No hay libros prestados actualmente.")
        else:
            print("\nLibros prestados:")
            for libro in self.libros_prestados:
                print(f' - "{libro["titulo"]}" de {libro["autor"]}')


def menu():
    biblioteca = Biblioteca()

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
                print("Programa finalizado.")
                break
            case _:
                print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    menu()
