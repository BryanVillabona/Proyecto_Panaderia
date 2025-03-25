import json

detalles_pedido = {}
pedidos = {}
productos_pan = {}
productos_pasteles = {}
productos_postres = {}

def cargar_datos(archivo):
    datos = {}
    try:
        with open(archivo, "r") as file:
            datos = json.load(file)
    except Exception:
        print("No se pudo cargar datos....")
        datos = None
    if archivo == "Proyecto_Panaderia/detalles_pedido.json":
        detalles_pedido.update(datos)
    elif archivo == "Proyecto_Panaderia/pedidos.json":
        pedidos.update(datos)
    elif archivo == "Proyecto_Panaderia/productos_pan.json":
        productos_pan.update(datos)
    elif archivo == "Proyecto_Panaderia/productos_pasteles.json":
        productos_pasteles.update(datos)
    elif archivo == "Proyecto_Panaderia/productos_postres.json":
        productos_postres.update(datos)

def guardar_datos(datos, archivo):
    try:
        datos_a_guardar = json.dumps(datos, indent=4)
        with open(archivo, "w") as file:
            file.write(datos_a_guardar)
    except Exception:
        print("No se pudo guardar datos....")

