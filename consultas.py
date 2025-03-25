from data import *

def buscar_producto_por_nombre():
    productos_totales = {**productos_pan, **productos_pasteles, **productos_postres}

    if not productos_totales:
        print("No hay productos registrados en el inventario.")
        return

    nombre_producto = input("Ingrese el nombre del producto que desea buscar: ").strip().capitalize()

    encontrado = None
    for codigo, datos in productos_totales.items():
        if datos["nombre"].capitalize() == nombre_producto:
            encontrado = (codigo, datos)
            break

    if encontrado:
        codigo, datos = encontrado
        print("\n===== Producto encontrado =====")
        print(f"Código: {codigo}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Categoría: {datos['categoria']}")
        print(f"Descripción: {datos['descripcion']}")
        print(f"Proveedor: {datos['proveedor']}")
        print(f"Cantidad en stock: {datos['cantidad_en_stock']}")
        print(f"Precio de venta: {datos['precio_venta']:.2f}")
        print(f"Precio del proveedor: {datos['precio_proveedor']:.2f}")
        print("===========================================")
    else:
        print("Producto no encontrado en el inventario.")

def buscar_por_categoria():
    productos_totales = {**productos_pan, **productos_pasteles, **productos_postres}

    if not productos_totales:
        print("No hay productos registrados en el inventario.")
        return

    print("\n========== Menú de Categorías ==========")
    print("1. Pan")
    print("2. Pasteles")
    print("3. Postres")
    print("=========================================")

    opcion = input("Seleccione una opción (1-3): ").strip()

    categorias = {"1": "Pan", "2": "Pasteles", "3": "Postres"}

    if opcion not in categorias:
        print("Error. Opción inválida. Debe elegir 1, 2 o 3.")
        return

    categoria_buscada = categorias[opcion]

    productos_encontrados = [
        (codigo, datos) for codigo, datos in productos_totales.items() if datos["categoria"] == categoria_buscada
    ]

    if productos_encontrados:
        print(f"\n===== Productos encontrados en la categoría '{categoria_buscada}' =====")
        for codigo, datos in productos_encontrados:
            print("-------------------------------------------")
            print(f"Código: {codigo}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Descripción: {datos['descripcion']}")
            print(f"Proveedor: {datos['proveedor']}")
            print(f"Cantidad en stock: {datos['cantidad_en_stock']}")
            print(f"Precio de venta: {datos['precio_venta']:.2f}")
            print(f"Precio del proveedor: {datos['precio_proveedor']:.2f}")
        print("===========================================")
    else:
        print(f"No hay productos registrados en la categoría '{categoria_buscada}'.")

def buscar_por_codigo():
    productos_totales = {**productos_pan, **productos_pasteles, **productos_postres}

    if not productos_totales:
        print("No hay productos registrados en el inventario.")
        return

    codigo_buscado = input("Ingrese el código del producto a buscar: ").strip().upper()

    if codigo_buscado in productos_totales:
        datos = productos_totales[codigo_buscado]
        print("\n====== Producto encontrado ======")
        print("-------------------------------------------")
        print(f"Código: {codigo_buscado}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Categoría: {datos['categoria']}")
        print(f"Descripción: {datos['descripcion']}")
        print(f"Proveedor: {datos['proveedor']}")
        print(f"Cantidad en stock: {datos['cantidad_en_stock']}")
        print(f"Precio de venta: {datos['precio_venta']:.2f}")
        print(f"Precio del proveedor: {datos['precio_proveedor']:.2f}")
        print("-------------------------------------------")
    else:
        print("No se encontró ningún producto con ese código.")

def filtrar_por_codigo_pedido():
    if not pedidos:
        print("No hay pedidos registrados.")
        return

    codigo_buscado = input("Ingrese el código del pedido a buscar: ").strip().upper()

    if codigo_buscado in pedidos:
        datos_pedido = pedidos[codigo_buscado]
        print("\n====== Pedido encontrado ======")
        print("-------------------------------------------")
        print(f"Código de Pedido: {codigo_buscado}")
        print(f"Código de Cliente: {datos_pedido['codigo_cliente']}")
        print(f"Fecha del Pedido: {datos_pedido['fecha_pedido']}")
        print("Detalles del Pedido:")

        for detalle in datos_pedido["detalles_pedido"]:
            print("  ---------------------------------------")
            print(f"  Código de Producto: {detalle['codigo_producto']}")
            print(f"  Cantidad: {detalle['cantidad']}")
            print(f"  Precio por Unidad: {detalle['precio_unidad']:.2f}")
            print(f"  Número de Línea: {detalle['numero_linea']}")

        print("-------------------------------------------")
    else:
        print("No se encontró ningún pedido con ese código.")

def filtrar_por_producto_incluido():
    if not pedidos:
        print("No hay pedidos registrados.")
        return

    codigo_producto_buscado = input("Ingrese el código del producto a buscar en los pedidos: ").strip().upper()
    pedidos_encontrados = []

    for codigo_pedido, datos_pedido in pedidos.items():
        for detalle in datos_pedido["detalles_pedido"]:
            if detalle["codigo_producto"] == codigo_producto_buscado:
                pedidos_encontrados.append((codigo_pedido, datos_pedido, detalle))

    if pedidos_encontrados:
        print("\nPedidos que incluyen el producto buscado:")
        print("===============================================")
        for codigo_pedido, datos_pedido, detalle in pedidos_encontrados:
            print(f"Código de Pedido: {codigo_pedido}")
            print(f"Código de Cliente: {datos_pedido['codigo_cliente']}")
            print(f"Fecha del Pedido: {datos_pedido['fecha_pedido']}")
            print("Detalles del Producto:")
            print(f"  Código de Producto: {detalle['codigo_producto']}")
            print(f"  Cantidad: {detalle['cantidad']}")
            print(f"  Precio por Unidad: {detalle['precio_unidad']:.2f}")
            print(f"  Número de Línea: {detalle['numero_linea']}")
            print("===============================================")
    else:
        print("❌ No se encontró ningún pedido que incluya este producto.")

