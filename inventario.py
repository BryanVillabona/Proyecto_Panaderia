from data import productos_pan, productos_pasteles, productos_postres

def ver_panes():   
    if not productos_pan:
        print("No hay productos registrados en el inventario.")
        return
    
    print("\n========== Inventario de Productos ==========")
    total_cantidad = 0
    limite_alerta = 5 

    for codigo, datos in productos_pan.items():
        nombre = datos["nombre"]
        cantidad = datos["cantidad_en_stock"]
        total_cantidad += cantidad

        print(f"Producto: {nombre} | Cantidad en stock: {cantidad}", end="")

        if cantidad <= limite_alerta:
            print(" | ⚠️  Quedan pocas unidades!")
        else:
            print()

    print("==============================================")
    print(f"Total de panes en inventario: {total_cantidad}")

def ver_pasteles():
    if not productos_pasteles:
        print("No hay productos registrados en el inventario.")
        return
    
    print("\n========== Inventario de Pasteles ==========")
    total_cantidad = 0
    limite_alerta = 5 

    for codigo, datos in productos_pasteles.items():
        nombre = datos["nombre"]
        cantidad = datos["cantidad_en_stock"]
        total_cantidad += cantidad

        print(f"Producto: {nombre} | Cantidad en stock: {cantidad}", end="")

        if cantidad <= limite_alerta:
            print(" | ⚠️  Quedan pocas unidades!")
        else:
            print()

    print("==============================================")
    print(f"Total de pasteles en inventario: {total_cantidad}")

def ver_postres():
    if not productos_postres:
        print("No hay productos registrados en el inventario.")
        return
    
    print("\n========== Inventario de Productos ==========")
    total_cantidad = 0
    limite_alerta = 5

    for codigo, datos in productos_postres.items():
        nombre = datos["nombre"]
        cantidad = datos["cantidad_en_stock"]
        total_cantidad += cantidad

        print(f"Producto: {nombre} | Cantidad en stock: {cantidad}", end="")

        if cantidad <= limite_alerta:
            print(" | ⚠️  Quedan pocas unidades!")
        else:
            print()

    print("==============================================")
    print(f"Total de postres en inventario: {total_cantidad}")

def modificar_inventario():
    productos_totales = {**productos_pan, **productos_pasteles, **productos_postres}

    if not productos_totales:
        print("No hay productos registrados en el inventario.")
        return
    
    print("\n========== Productos Disponibles ==========")
    for codigo, datos in productos_totales.items():
        print(f"{codigo}: {datos['nombre']} | Stock actual: {datos['cantidad_en_stock']}")
    print("===========================================")

    codigo_producto = input("Ingrese el código del producto que desea modificar: ").strip()

    if codigo_producto in productos_pan:
        producto = productos_pan[codigo_producto]
    elif codigo_producto in productos_pasteles:
        producto = productos_pasteles[codigo_producto]
    elif codigo_producto in productos_postres:
        producto = productos_postres[codigo_producto]
    else:
        print("Error: El código ingresado no existe en el inventario.")
        return

    while True:
        try:
            nuevo_stock = int(input(f"Ingrese la nueva cantidad en stock para '{producto['nombre']}': "))
            if nuevo_stock < 0:
                print("Error. La cantidad en stock no puede ser negativa. Intente nuevamente.")
            else:
                producto["cantidad_en_stock"] = nuevo_stock
                print("\nStock ha sido actualizado:")
                print(f"Nombre: {producto['nombre']}")
                print(f"Nuevo stock: {producto['cantidad_en_stock']}")
                print("===========================================")
                break
        except ValueError:
            print("Error: Ingrese un número válido.")

def eliminar_producto():
    productos_totales = {**productos_pan, **productos_pasteles, **productos_postres}

    if not productos_totales:
        print("No hay productos registrados en el inventario.")
        return
    
    print("\n========== Productos Disponibles ==========")
    for codigo, datos in productos_totales.items():
        print(f"{codigo}: {datos['nombre']} | Stock: {datos['cantidad_en_stock']}")
    print("===========================================")

    codigo_producto = input("Ingrese el código del producto que desea eliminar: ").strip()

    if codigo_producto in productos_pan:
        producto_eliminado = productos_pan.pop(codigo_producto)
    elif codigo_producto in productos_pasteles:
        producto_eliminado = productos_pasteles.pop(codigo_producto)
    elif codigo_producto in productos_postres:
        producto_eliminado = productos_postres.pop(codigo_producto)
    else:
        print("Error: El código ingresado no existe en el inventario.")
        return

    print("\n====== Producto eliminado con éxito ======")
    print(f"Nombre: {producto_eliminado['nombre']}")
    print(f"Categoría: {producto_eliminado['categoria']}")
    print(f"Cantidad en stock: {producto_eliminado['cantidad_en_stock']}")
    print(f"Precio de venta: {producto_eliminado['precio_venta']:.2f}")
    print("===========================================")

