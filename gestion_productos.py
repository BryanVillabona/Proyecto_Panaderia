from data import productos_pan, productos_pasteles, productos_postres

def registrar_producto_pan():
    try:
        codigo = f"PN-{len(productos_pan) + 1:03d}"
        codigo_producto = codigo

        nom_producto = input("Digite el nombre del producto: ").strip().capitalize()
        if not nom_producto:
            raise ValueError("El nombre del producto no puede estar vacío.")

        descripcion = input("Descripción del producto: ").strip().capitalize()
        if not descripcion:
            raise ValueError("La descripción no puede estar vacía.")

        proveedor = input("Proveedor del producto: ").strip().capitalize()
        if not proveedor:
            raise ValueError("El proveedor no puede estar vacío.")

        while True:
            try:
                cantidad_stock = int(input("Digite cantidad en stock del producto: "))
                if cantidad_stock < 0:
                    print("La cantidad en stock no puede ser negativa. Inténte nuevamente.")
                else:
                    break
            except ValueError:
                print("Error: Ingrese un número entero válido para la cantidad en stock.")

        while True:
            try:
                precio_venta = float(input("Digite el precio de venta del producto: "))
                if precio_venta <= 0:
                    print("El precio de venta debe ser un valor positivo. Inténte nuevamente.")
                else:
                    break
            except ValueError:
                print("Error: Ingrese un valor numérico válido para el precio de venta.")

        while True:
            try:
                precio_proveedor = float(input("Digite el precio por parte del proveedor: "))
                if precio_proveedor <= 0:
                    print("El precio del proveedor debe ser un valor positivo. Inténte nuevamente.")
                else:
                    break
            except ValueError:
                print("Error: Ingrese un valor numérico válido para el precio del proveedor.")

        productos_pan[codigo_producto] = {
            "nombre": nom_producto,
            "categoria": "Pan",
            "descripcion": descripcion,
            "proveedor": proveedor,
            "cantidad_en_stock": cantidad_stock,
            "precio_venta": precio_venta,
            "precio_proveedor": precio_proveedor
        }

        print("\n====== Producto registrado con éxito ======")
        print("--------------------------------")
        print(f"Código: {codigo_producto}")
        print(f"Nombre: {nom_producto}")
        print(f"Categoría: Pan")
        print(f"Descripción: {descripcion}")
        print(f"Proveedor: {proveedor}")
        print(f"Cantidad en Stock: {cantidad_stock}")
        print(f"Precio de Venta: {precio_venta:.2f}")
        print(f"Precio del Proveedor: {precio_proveedor:.2f}")
        print("--------------------------------")

    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")

def registrar_producto_pasteles():
    try:
        codigo = f"PS-{len(productos_pasteles) + 1:03d}"
        codigo_producto = codigo

        nom_producto = input("Digite el nombre del producto: ").strip().capitalize()
        if not nom_producto:
            raise ValueError("El nombre del producto no puede estar vacío.")

        descripcion = input("Descripción del producto: ").strip().capitalize()
        if not descripcion:
            raise ValueError("La descripción no puede estar vacía.")

        proveedor = input("Proveedor del producto: ").strip().capitalize()
        if not proveedor:
            raise ValueError("El proveedor no puede estar vacío.")

        try:
            cantidad_stock = int(input("Digite cantidad en stock del producto: "))
            if cantidad_stock < 0:
                raise ValueError("La cantidad en stock no puede ser negativa.")
        except ValueError:
            raise ValueError("Debe ingresar un número entero válido para la cantidad en stock.")

        try:
            precio_venta = float(input("Digite el precio de venta del producto: "))
            if precio_venta <= 0:
                raise ValueError("El precio de venta debe ser mayor a 0.")
        except ValueError:
            raise ValueError("Debe ingresar un número válido para el precio de venta.")

        try:
            precio_proveedor = float(input("Digite el precio por parte del proveedor: "))
            if precio_proveedor <= 0:
                raise ValueError("El precio del proveedor debe ser mayor a 0.")
        except ValueError:
            raise ValueError("Debe ingresar un número válido para el precio del proveedor.")

        productos_pasteles[codigo_producto] = {
            "nombre": nom_producto,
            "categoria": "Pasteles",
            "descripcion": descripcion,
            "proveedor": proveedor,
            "cantidad_en_stock": cantidad_stock,
            "precio_venta": precio_venta,
            "precio_proveedor": precio_proveedor
        }
        print("====== Producto Registrado ======")
    
    except ValueError as e:
        print(f"Error: {e}")

def registrar_producto_postres():
    try:
        codigo = f"PT-{len(productos_postres) + 1:03d}"
        codigo_producto = codigo

        nom_producto = input("Digite el nombre del producto: ").strip().capitalize()
        if not nom_producto:
            raise ValueError("El nombre del producto no puede estar vacío.")

        descripcion = input("Descripción del producto: ").strip().capitalize()
        if not descripcion:
            raise ValueError("La descripción no puede estar vacía.")

        proveedor = input("Proveedor del producto: ").strip().capitalize()
        if not proveedor:
            raise ValueError("El proveedor no puede estar vacío.")

        try:
            cantidad_stock = int(input("Digite cantidad en stock del producto: "))
            if cantidad_stock < 0:
                raise ValueError("La cantidad en stock no puede ser negativa.")
        except ValueError:
            raise ValueError("Debe ingresar un número entero válido para la cantidad en stock.")

        try:
            precio_venta = float(input("Digite el precio de venta del producto: "))
            if precio_venta <= 0:
                raise ValueError("El precio de venta debe ser mayor a 0.")
        except ValueError:
            raise ValueError("Debe ingresar un número válido para el precio de venta.")

        try:
            precio_proveedor = float(input("Digite el precio por parte del proveedor: "))
            if precio_proveedor <= 0:
                raise ValueError("El precio del proveedor debe ser mayor a 0.")
        except ValueError:
            raise ValueError("Debe ingresar un número válido para el precio del proveedor.")

        productos_postres[codigo_producto] = {
            "nombre": nom_producto,
            "categoria": "Postres",
            "descripcion": descripcion,
            "proveedor": proveedor,
            "cantidad_en_stock": cantidad_stock,
            "precio_venta": precio_venta,
            "precio_proveedor": precio_proveedor
        }
        print("====== Producto Registrado ======")
    
    except ValueError as e:
        print(f"Error: {e}")

def modificar_producto():
    codigo_producto = input("Digite el código del producto que desea editar: ").upper()

    productos_totales = {**productos_pan, **productos_pasteles, **productos_postres}
    
    if codigo_producto not in productos_totales:
        print("Este producto no existe")
        return
    
    producto = productos_totales[codigo_producto]
    
    try:
        nom_producto = input("Digite el nombre del producto: ").strip().capitalize()
        if not nom_producto:
            raise ValueError("El nombre del producto no puede estar vacío.")

        descripcion = input("Descripción del producto: ").strip().capitalize()
        if not descripcion:
            raise ValueError("La descripción no puede estar vacía.")

        proveedor = input("Proveedor del producto: ").strip().capitalize()
        if not proveedor:
            raise ValueError("El proveedor no puede estar vacío.")

        cantidad_stock = int(input("Digite cantidad en stock del producto: "))
        if cantidad_stock < 0:
            raise ValueError("La cantidad en stock no puede ser negativa.")

        precio_venta = float(input("Digite el precio de venta del producto: "))
        if precio_venta <= 0:
            raise ValueError("El precio de venta debe ser mayor a 0.")

        precio_proveedor = float(input("Digite el precio por parte del proveedor: "))
        if precio_proveedor <= 0:
            raise ValueError("El precio del proveedor debe ser mayor a 0.")
        
        categoria = ""
        if codigo_producto.startswith("PN-"):
            categoria = "Pan"
            productos_pan[codigo_producto].update({
                "nombre": nom_producto,
                "categoria": categoria,
                "descripcion": descripcion,
                "proveedor": proveedor,
                "cantidad_en_stock": cantidad_stock,
                "precio_venta": precio_venta,
                "precio_proveedor": precio_proveedor
            })
        elif codigo_producto.startswith("PS-"):
            categoria = "Pasteles"
            productos_pasteles[codigo_producto].update({
                "nombre": nom_producto,
                "categoria": categoria,
                "descripcion": descripcion,
                "proveedor": proveedor,
                "cantidad_en_stock": cantidad_stock,
                "precio_venta": precio_venta,
                "precio_proveedor": precio_proveedor
            })
        elif codigo_producto.startswith("PT-"):
            categoria = "Postres"
            productos_postres[codigo_producto].update({
                "nombre": nom_producto,
                "categoria": categoria,
                "descripcion": descripcion,
                "proveedor": proveedor,
                "cantidad_en_stock": cantidad_stock,
                "precio_venta": precio_venta,
                "precio_proveedor": precio_proveedor
            })
        
        print("========== Producto Modificado ==========")
    except ValueError as e:
        print(f"Error: {e}")
    
def listar_productos():
    productos_totales = {**productos_pan, **productos_pasteles, **productos_postres}

    if not productos_totales:
        print("No hay productos registrados en el inventario.")
        return
    
    print("\n========== Lista de Productos Registrados ==========")
    for codigo, datos in productos_totales.items():
        print(f"Código: {codigo}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Categoría: {datos['categoria']}")
        print(f"Descripción: {datos['descripcion']}")
        print(f"Proveedor: {datos['proveedor']}")
        print(f"Cantidad en stock: {datos['cantidad_en_stock']}")
        print(f"Precio de venta: ${datos['precio_venta']:.2f}")
        print(f"Precio proveedor: ${datos['precio_proveedor']:.2f}")
        print("====================================================")
