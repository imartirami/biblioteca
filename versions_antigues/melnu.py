class Biblioteca:
    def __init__ (self):
        self.total_libros = 0
        self.libros = []
    
    def agregar_libro(self, titulo, autor):
        self.libros.append({"titulo":titulo, "autor":autor, "disponible": True})
        print(f'Título: {titulo} agregado correctamente')
        self.total_libros += 1
    
    def mostrar_libros (self,libros):
        if not libros:
            print ('La lista está vacía')
        else:
            print(f'Hay {self.total_libros} libros en la biblioteca.')
            for libro in libros:
                print(f'{libro["titulo"]}, {libro["autor"]}, {libro["disponible"]}')
    
    def prestar_libro (self, titulo, libros, total_libros):
        self.libros_prestados = []
        if not libros:
            print ('La lista está vacía')
        else:
            for l,libro in enumerate(libros):
                if titulo == libro['titulo']:
                    self.libros_prestados.append(libro)
                    print(f'Has retirado el libro {libro['titulo']}.')
                    del libros[l]
                    self.total_libros -= 1
            
    def devolver_libro (self, titulo, autor, total_libros):
        #self.libros_prestados = []
        
        self.libros.append({"titulo":titulo, "autor":autor, "disponible": True})
        print(f'Título: {titulo} devuelto correctamente')
        self.total_libros += 1
        print(f'Cantidad libros: {self.total_libros}')
    
    def buscar_por_autor(self, autor):
        encontrados = []

        for libro in self.libros:
            if libro["autor"].lower() == autor.lower():
                encontrados.append(libro)

        if encontrados:
            print("\nLibros encontrados:")
            for libro in encontrados:
                estado = "Disponible" if libro["disponible"] else "Prestado"
                print(f" - {libro['titulo']} ({estado})")
        else:
            print("No se encontraron libros de ese autor.")

    #def menu(self):
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
                    self.mostrar_libros(self.libros)
                case "3":
                    autor = input("Nombre del autor: ")
                    self.buscar_por_autor(autor)
                case "4":
                    titulo = input("Título del libro a prestar: ")
                    if not self.libros:
                        print('No hay libros que prestar')
                    else:
                        self.prestar_libro(titulo, self.libros, self.total_libros)
                case "5":
                    titulo = input("Título del libro a devolver: ")
                    self.devolver_libro(titulo, self.libros, self.total_libros)
                case "6":
                    print(" Saliendo del sistema...")
                    break
                case _:
                    print(" Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    biblioteca = Biblioteca()
    #biblioteca.menu()