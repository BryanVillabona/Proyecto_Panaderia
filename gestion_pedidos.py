from data import detalles_pedido, productos_pan, productos_pasteles,productos_postres, pedidos
from gestion_productos import *
from datetime import datetime

def registrar_pedido():
    nuevo_codigo = f"P{len(detalles_pedido) + 1:04d}" 

    if nuevo_codigo not in detalles_pedido:
        detalles_pedido[nuevo_codigo] = [] 

    numero_linea = len(detalles_pedido[nuevo_codigo]) + 1 
    productos_totales = {**productos_pan, **productos_pasteles, **productos_postres}

    codigo_pedido_nuevo = f"P{len(pedidos) + 1:03d}"
    codigo_cliente = f"CL-{len(pedidos) + 1:03d}"
    fecha_pedido = datetime.now().strftime("%Y-%m-%d")

    while True:
        print("\n=== LISTA DE PRODUCTOS DISPONIBLES ===")
        for llave, datos in productos_totales.items():
            print(f"Producto: {datos['nombre']}\nCantidad en stock: {datos['cantidad_en_stock']}\nPrecio: {datos['precio_venta']}")
            print("===========================================")

        elegir = input("¿Qué desea comprar? (O escriba 'salir' para finalizar): ").capitalize()
        if elegir.lower() == "salir":
            if detalles_pedido[nuevo_codigo]: 
                pedidos[codigo_pedido_nuevo] = {
                    "codigo_cliente": codigo_cliente,
                    "fecha_pedido": fecha_pedido,
                    "detalles_pedido": detalles_pedido[nuevo_codigo]
                }
                print(f"Pedido registrado correctamente con código {codigo_pedido_nuevo}.")
            else:
                print("No se registró ningún pedido.")
            break

        producto_encontrado = None
        for llave, datos in productos_totales.items():
            if datos['nombre'].capitalize() == elegir:
                producto_encontrado = (llave, datos)
                break

        if producto_encontrado:
            llave, datos = producto_encontrado
            while True:
                try:
                    cantidad = int(input(f"¿Cuántos '{elegir}' desea comprar?: "))
                    if cantidad <= 0:
                        print("Por favor, ingrese una cantidad válida.")
                    elif cantidad > datos['cantidad_en_stock']:
                        print(f"Lo sentimos, solo tenemos {datos['cantidad_en_stock']} unidades disponibles.")
                    else:
                        datos['cantidad_en_stock'] -= cantidad
                        print(f"Has comprado {cantidad} '{elegir}'. Quedan {datos['cantidad_en_stock']} en stock.")

                        pedido = {
                            "codigo_pedido": int(nuevo_codigo[1:]), 
                            "codigo_producto": llave,
                            "cantidad": cantidad,
                            "precio_unidad": datos["precio_venta"],
                            "numero_linea": numero_linea
                        }

                        detalles_pedido[nuevo_codigo].append(pedido)
                        numero_linea += 1 
                        print(f"Producto agregado al pedido: {pedido}")
                        break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        else:
            print("Este producto no existe.")

def ver_pedidos():
    if not pedidos:
        print("No hay ningún pedido registrado.")
        return 

    print("\n========== Pedidos Registrados ==========")

    for codigo_pedido, datos in pedidos.items():
        print(f"\nCódigo de Pedido: {codigo_pedido}")
        print(f"Código de Cliente: {datos['codigo_cliente']}")
        print(f"Fecha del Pedido: {datos['fecha_pedido']}")
        print("\n--- Detalles del Pedido ---")
        
        if not datos["detalles_pedido"]:
            print("   No hay productos en este pedido.")
        else:
            for detalle in datos["detalles_pedido"]:
                print(f"   Producto: {detalle['codigo_producto']}")
                print(f"   Cantidad: {detalle['cantidad']}")
                print(f"   Precio por unidad: {detalle['precio_unidad']:.2f}")
                print(f"   Número de línea: {detalle['numero_linea']}")
                print("   -----------------------")

        print("===========================================")

def modificar_pedido():
    if not pedidos:
        print("No hay pedidos registrados para modificar.")
        return

    print("\n========== Pedidos Disponibles ==========")
    for codigo_pedido in pedidos.keys():
        print(f"- {codigo_pedido}")
    print("===========================================")

    codigo_pedido = input("Ingrese el código del pedido que desea modificar: ").strip().capitalize()

    if codigo_pedido not in pedidos:
        print("El código de pedido ingresado no existe.")
        return

    pedido = pedidos[codigo_pedido]
    detalles = pedido["detalles_pedido"]

    while True:
        print("\n--- Detalles del Pedido ---")
        for i, detalle in enumerate(detalles, start=1):
            print(f"{i}. Producto: {detalle['codigo_producto']} | Cantidad: {detalle['cantidad']} | Precio: {detalle['precio_unidad']:.2f}")

        print("\nOpciones:")
        print("1. Modificar cantidad de un producto")
        print("2. Eliminar un producto del pedido")
        print("3. Agregar un nuevo producto al pedido")
        print("4. Salir y guardar cambios")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                indice = int(input("Ingrese el número del producto que desea modificar: ")) - 1
                if 0 <= indice < len(detalles):
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    if nueva_cantidad > 0:
                        detalles[indice]["cantidad"] = nueva_cantidad
                        print("Cantidad actualizada correctamente.")
                    else:
                        print("La cantidad debe ser mayor que 0.")
                else:
                    print("Número de producto inválido.")
            except ValueError:
                print("Ingrese un número válido.")

        elif opcion == "2":
            try:
                indice = int(input("Ingrese el número del producto que desea eliminar: ")) - 1
                if 0 <= indice < len(detalles):
                    detalles.pop(indice)
                    print("Producto eliminado correctamente.")
                else:
                    print("Número de producto inválido.")
            except ValueError:
                print("Ingrese un número válido.")

        elif opcion == "3":
            productos_totales = {**productos_pan, **productos_pasteles, **productos_postres}

            print("\n=== LISTA DE PRODUCTOS DISPONIBLES ===")
            for llave, datos in productos_totales.items():
                print(f"Producto: {datos['nombre']} | Stock: {datos['cantidad_en_stock']} | Precio: {datos['precio_venta']:.2f}")

            nuevo_producto = input("Ingrese el nombre del nuevo producto: ").capitalize()

            producto_encontrado = None
            for llave, datos in productos_totales.items():
                if datos['nombre'].capitalize() == nuevo_producto:
                    producto_encontrado = (llave, datos)
                    break

            if producto_encontrado:
                llave, datos = producto_encontrado
                try:
                    cantidad = int(input(f"Ingrese la cantidad de '{nuevo_producto}': "))
                    if cantidad > 0 and cantidad <= datos["cantidad_en_stock"]:
                        datos["cantidad_en_stock"] -= cantidad
                        detalles.append({
                            "codigo_pedido": int(codigo_pedido[1:]),
                            "codigo_producto": llave,
                            "cantidad": cantidad,
                            "precio_unidad": datos["precio_venta"],
                            "numero_linea": len(detalles) + 1
                        })
                        print(f"Producto '{nuevo_producto}' agregado correctamente.")
                    else:
                        print("Cantidad inválida o insuficiente en stock.")
                except ValueError:
                    print("Ingrese una cantidad válida.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            print("Guardando cambios en el pedido...")
            pedidos[codigo_pedido]["detalles_pedido"] = detalles
            print("Pedido actualizado correctamente.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

def eliminar_pedido():
    if not pedidos:
        print("No hay pedidos registrados para eliminar.")
        return

    print("\n========== Pedidos Disponibles ==========")
    for codigo_pedido in pedidos.keys():
        print(f"- {codigo_pedido}")
    print("===========================================")

    codigo_pedido = input("Ingrese el código del pedido que desea eliminar: ").strip().capitalize()

    if codigo_pedido not in pedidos:
        print("El código de pedido ingresado no existe.")
        return

    pedido_eliminado = pedidos[codigo_pedido]
    print("\n=== Detalles del Pedido a Eliminar ===")
    print(f"Código de Pedido: {codigo_pedido}")
    print(f"Código de Cliente: {pedido_eliminado['codigo_cliente']}")
    print(f"Fecha del Pedido: {pedido_eliminado['fecha_pedido']}")
    print("Productos:")
    for detalle in pedido_eliminado["detalles_pedido"]:
        print(f"  - Producto: {detalle['codigo_producto']} | Cantidad: {detalle['cantidad']} | Precio: {detalle['precio_unidad']:.2f}")
    print("========================================")

    confirmacion = input(f"¿Está seguro de que desea eliminar el pedido {codigo_pedido}? (sí/no): ").strip().lower()

    if confirmacion == "si" or confirmacion == "sí":
        pedido_eliminado = pedidos.pop(codigo_pedido)

        detalles_pedido.pop(codigo_pedido, None)

        print("\nPedido eliminado correctamente. Datos eliminados:")
        print(pedido_eliminado) 
    else:
        print("Eliminación cancelada.")

