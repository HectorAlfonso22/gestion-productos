import os

# Lista de productos almacenada como una lista de diccionarios
productos = []

def cargar_datos():
    """Carga los datos de productos desde un archivo de texto."""
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(", ")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
        print("Datos cargados correctamente.")
    else:
        print("No se encontró el archivo 'productos.txt'. Iniciando con una lista vacía.")

def guardar_datos():
    """Guarda los datos de productos en un archivo de texto."""
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")
    print("Datos guardados correctamente.")

def añadir_producto():
    """Permite al usuario añadir un nuevo producto."""
    nombre = input("Introduce el nombre del producto: ").strip()
    try:
        precio = float(input("Introduce el precio del producto: "))
        cantidad = int(input("Introduce la cantidad disponible del producto: "))
    except ValueError:
        print("Precio y cantidad deben ser numéricos.")
        return

    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto '{nombre}' añadido correctamente.")

def ver_productos():
    """Muestra todos los productos almacenados."""
    if not productos:
        print("No hay productos disponibles.")
    else:
        print("Lista de productos:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    """Permite al usuario actualizar un producto existente."""
    nombre = input("Introduce el nombre del producto a actualizar: ").strip()
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            try:
                nuevo_nombre = input("Introduce el nuevo nombre del producto (o presiona Enter para mantener el actual): ").strip()
                nuevo_precio = input("Introduce el nuevo precio del producto (o presiona Enter para mantener el actual): ").strip()
                nueva_cantidad = input("Introduce la nueva cantidad del producto (o presiona Enter para mantener la actual): ").strip()

                if nuevo_nombre:
                    producto["nombre"] = nuevo_nombre
                if nuevo_precio:
                    producto["precio"] = float(nuevo_precio)
                if nueva_cantidad:
                    producto["cantidad"] = int(nueva_cantidad)

                print(f"Producto '{producto['nombre']}' actualizado correctamente.")
            except ValueError:
                print("Precio y cantidad deben ser numéricos.")
            return

    print(f"No se encontró un producto con el nombre '{nombre}'.")

def eliminar_producto():
    """Permite al usuario eliminar un producto."""
    nombre = input("Introduce el nombre del producto a eliminar: ").strip()
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return

    print(f"No se encontró un producto con el nombre '{nombre}'.")

def menu():
    """Muestra el menú principal y gestiona las opciones."""
    while True:
        print("\nSistema de Gestión de Productos")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    cargar_datos()
    menu()
