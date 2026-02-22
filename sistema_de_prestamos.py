prestamos = {}
def registrar_prestamo():
    nombre = input("ingrese el nombre de la persona: ").capitalize()
    libro = input("ingrese el nombre del libro: ").capitalize()
    if nombre in prestamos:
        print("esta persona ya tiene un libro prestado.")
    else:
        prestamos[nombre] = libro
        print(f"prestamo registrado: {nombre} → '{libro}'")
def devolver_libro():
    nombre = input("ingrese el nombre de la persona que devuelve el libro: ").capitalize()
    if nombre in prestamos:
        libro = prestamos[nombre]
        del prestamos[nombre]
        print(f"libro '{libro}' devuelto correctamente por {nombre}.")
    else:
        print("no se encontro ningun prestamo registrado para esa persona.")
def mostrar_prestamos():
    if not prestamos:
        print("no hay prestamos activos.")
        return
    print("\n prestamos activios:")
    for nombre, libro in prestamos.items():
        print(f"- {nombre} tiene prestado: '{libro}'")
def menu():
    while True:
        print("\n sistema de prestamos ")
        print("1. registrar prestamo")
        print("2. devolver libro")
        print("3. mostrar préstamos")
        print("4. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            registrar_prestamo()
        elif opcion == "2":
            devolver_libro()
        elif opcion == "3":
            mostrar_prestamos()
        elif opcion == "4":
            print("saliendo del sistema de prestamos.")
            break
        else:
            print("opcion invalida, intente nuevamente.")
menu()