def solicitar_credenciales():
    usuario_correcto = "admin"
    clave_correcta = "1234"
    print("Bienvenido al Sistema de Gestión de Inventario")
    
    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
        
        if usuario == usuario_correcto and clave == clave_correcta:
            print("Acceso concedido. ¡Bienvenido!")
            break
        else:
            print("Usuario o clave incorrectos. Por favor, inténtelo nuevamente.")

def mostrar_menu():
    opciones = [
        "1. Agregar producto al inventario",
        "2. Modificar un producto o su cantidad",
        "3. Eliminar un producto",
        "4. Mostrar productos en el inventario",
        "5. Salir"
    ]
    print("\nMenú de Gestión de Inventario")
    for opcion in opciones:
        print(opcion)

def agregar_producto(inventario):
    print("\nAgregar Producto (Escriba 'salir' en cualquier momento para volver al menú principal)")
    nombre = input("Ingrese el nombre del producto: ")
    if nombre.lower() == "salir":
        return

    while True:
        cantidad = input(f"Ingrese la cantidad de '{nombre}': ")
        if cantidad.lower() == "salir":
            return

        if cantidad.isdigit():
            inventario.append({'nombre': nombre, 'cantidad': int(cantidad)})
            print(f"Producto '{nombre}' agregado exitosamente.")
            break
        else:
            print("Por favor, ingrese un número válido o escriba 'salir'.")

def modificar_producto(inventario):
    if not inventario:
        print("\nEl inventario está vacío.")
        return

    print("\nModificar Producto")
    mostrar_inventario(inventario)
    while True:
        seleccion = input("\nSeleccione el número del producto que desea modificar (o escriba 'salir' para regresar): ")
        if seleccion.lower() == "salir":
            return

        if seleccion.isdigit() and 1 <= int(seleccion) <= len(inventario):
            producto = inventario[int(seleccion) - 1]
            print(f"Ha seleccionado: {producto['nombre']} - Cantidad: {producto['cantidad']}")

            confirmar = input("¿Está seguro de que desea modificar este producto? (s/n): ").lower()
            if confirmar == "s":
                nuevo_nombre = input(f"Ingrese el nuevo nombre para '{producto['nombre']}' (o presione Enter para mantenerlo igual): ")
                if nuevo_nombre:
                    producto['nombre'] = nuevo_nombre

                while True:
                    nueva_cantidad = input(f"Ingrese la nueva cantidad para '{producto['nombre']}' (o presione Enter para mantenerla igual): ")
                    if nueva_cantidad.lower() == "salir":
                        return

                    if nueva_cantidad == "":
                        break

                    if nueva_cantidad.isdigit():
                        producto['cantidad'] = int(nueva_cantidad)
                        break
                    else:
                        print("Por favor, ingrese un número válido o presione Enter para mantener la cantidad actual.")

                print(f"Producto modificado: {producto['nombre']} - Cantidad: {producto['cantidad']}")
            else:
                print("Modificación cancelada.")
            return
        else:
            print("Número fuera de rango o entrada inválida. Por favor, inténtelo nuevamente.")

def eliminar_producto(inventario):
    if not inventario:
        print("\nEl inventario está vacío.")
        return

    print("\nEliminar Producto")
    mostrar_inventario(inventario)
    while True:
        seleccion = input("\nSeleccione el número del producto que desea eliminar (o escriba 'salir' para regresar): ")
        if seleccion.lower() == "salir":
            return

        if seleccion.isdigit() and 1 <= int(seleccion) <= len(inventario):
            producto_eliminado = inventario[int(seleccion) - 1]

            confirmar = input(f"¿Está seguro de que desea eliminar el producto '{producto_eliminado['nombre']}'? (s/n): ").lower()
            if confirmar == "s":
                inventario.pop(int(seleccion) - 1)
                print(f"Producto eliminado: {producto_eliminado['nombre']}")
            else:
                print("Eliminación cancelada.")
            return
        else:
            print("Número fuera de rango o entrada inválida. Por favor, inténtelo nuevamente.")

def mostrar_inventario(inventario):
    if not inventario:
        print("\nEl inventario está vacío.")
    else:
        print("\nProductos en el inventario:")
        for i, producto in enumerate(inventario, start=1):
            print(f"{i}. {producto['nombre']} - Cantidad: {producto['cantidad']}")

    # Pausar hasta que el usuario presione Enter
    input("\nPresione Enter para regresar al menú principal.")

def main():
    # Solicitar credenciales antes de acceder al menú
    solicitar_credenciales()

    inventario = []  # Lista para almacenar los productos
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            modificar_producto(inventario)
        elif opcion == "3":
            eliminar_producto(inventario)
        elif opcion == "4":
            mostrar_inventario(inventario)
        elif opcion == "5":
            print("Saliendo del sistema de gestión de inventario. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, inténtelo nuevamente.")

if __name__ == "__main__":
    main()