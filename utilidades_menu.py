from gestion_productos import *
from gestion_pedidos import *
from inventario import *
from consultas import *

menu_principal = """
***************************************
1. Gestión de productos
2. Gestión de pedidos
3. Consultar inventario
4. Consultas
5. Salir
***************************************
"""

menu_productos = """
***************************************
1. Registrar producto
2. Listar productos
3. Editar producto
4. Regresar menu principal
***************************************
"""

menu_registro_producto = """
**** Qué producto desea registrar? ****
***************************************
1. Pan
2. Pastel
3. Postres
4. Regresar menu anterior
***************************************
"""

menu_pedidos = """
***************************************
1. Registrar pedido
2. Ver pedidos
3. Editar un pedido
4. Eliminar un pedido
5. Regresar menu principal
***************************************
"""

menu_inventario = """
***************************************
1. Inventario panes
2. Inventario postres
3. Inventario pasteles
4. Modificar
5. Eliminar
6. Regresar menu principal
***************************************
"""

menu_consultas = """
***************************************
1. Buscar producto
2. Filtrar pedido
3. Regresar menu principal
***************************************
"""

menu_buscar_producto = """
***************************************
1. Buscar producto por nombre
2. Buscar producto por categoria
3. Buscar producto por código 
4. Regresar al menu anterior
***************************************
"""

menu_filtrar_pedido = """
***************************************
1. Filtrar por código de pedido
2. Filtrar por producto incluido
3. Regresar al menu anterior
***************************************
"""

def mostrar_menu():
    return print(menu_principal)

def mostrar_menu_productos():
    return print(menu_productos)

def mostrar_menu_registro_productos():
    return print(menu_registro_producto)

def mostrar_menu_pedidos():
    return print(menu_pedidos)

def mostrar_menu_inventario():
    return print(menu_inventario)

def mostrar_menu_consultas():
    return print(menu_consultas)

def mostrar_menu_buscar_producto():
    return print(menu_buscar_producto)

def mostrar_menu_filtrar_pedido():
    return print(menu_filtrar_pedido)

def pedir_opcion():
    return int(input("Bienvenido. Elija una opción: "))

def ejecucion_menu_principal():
    while True:
        mostrar_menu()
        opc = pedir_opcion()
        match opc:
            case 1:
                submenu_productos()
            case 2:
                submenu_pedidos()
            case 3:
                submenu_inventario()
            case 4:
                submenu_consultas()
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Error. Elija una opcion válida")

def submenu_productos():
    while True:
        mostrar_menu_productos()
        opc_productos = pedir_opcion()
        match opc_productos:
            case 1:
                submenu_registro_productos()
            case 2:
                listar_productos()
            case 3:
                modificar_producto()
            case 4:
                print("Regresar menu principal")
                break
            case _:
                print("Error. Digite una opcion válida")

def submenu_registro_productos():
    while True:
        mostrar_menu_registro_productos()
        opc_reg_producto = pedir_opcion()
        match opc_reg_producto:
            case 1:
                registrar_producto_pan()
            case 2:
                registrar_producto_pasteles()
            case 3:
                registrar_producto_postres()
            case 4:
                print("Regresar menu principal")
                break
            case _:
                print("Error. Digite una opcion válida")

def submenu_pedidos():
    while True:
        mostrar_menu_pedidos()
        opc_pedidos = pedir_opcion()
        match opc_pedidos:
            case 1:
                registrar_pedido()
            case 2:
                ver_pedidos()
            case 3:
                modificar_pedido()
            case 4:
                eliminar_pedido()
            case 5:
                print("Regresar menu principal")
                break
            case _:
                print("Error. Digite una opcion válida")

def submenu_inventario():
    while True:
        mostrar_menu_inventario()
        opc_inventario = pedir_opcion()
        match opc_inventario:
            case 1:
                ver_panes()
            case 2:
                ver_postres()
            case 3:
                ver_pasteles()
            case 4:
                modificar_inventario()
            case 5:
                eliminar_producto()
            case 6:
                print("Regeresar al menu principal")
                break
            case _:
                print("Error. Digite una opcion válida")

def submenu_consultas():
    while True:
        mostrar_menu_consultas()
        opc_consultas = pedir_opcion()
        match opc_consultas:
            case 1:
                submenu_buscar_producto()
            case 2:
                submenu_filtrar_pedido()
            case 3:
                print("Regeresar al menu principal")
                break
            case _:
                print("Error. Digite una opcion válida")

def submenu_buscar_producto():
    while True:
        mostrar_menu_buscar_producto()
        opc_buscar_producto = pedir_opcion()
        match opc_buscar_producto:
            case 1:
                buscar_producto_por_nombre()
            case 2:
                buscar_por_categoria()
            case 3:
                buscar_por_codigo()
            case 4:
                print("Regresar al menu principal")
                break
            case _:
                print("Error. Digite una opcion válida")

def submenu_filtrar_pedido():
    while True:
        mostrar_menu_filtrar_pedido()
        opc_filtrar_pedido = pedir_opcion()
        match opc_filtrar_pedido:
            case 1:
                filtrar_por_codigo_pedido()
            case 2:
                filtrar_por_producto_incluido()
            case 3:
                print("Regresar al menu anterior")
                break
            case _:
                print("Error. Digite una opcion válida")