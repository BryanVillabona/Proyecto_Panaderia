from utilidades_menu import ejecucion_menu_principal
from data import *

cargar_datos("productos_pan.json")
cargar_datos("productos_pasteles.json")
cargar_datos("productos_postres.json")
cargar_datos("detalles_pedido.json")
cargar_datos("pedidos.json")
ejecucion_menu_principal()
guardar_datos(productos_pan, "productos_pan.json")
guardar_datos(productos_pasteles, "productos_pasteles.json")
guardar_datos(productos_postres, "productos_postres.json")
guardar_datos(detalles_pedido, "detalles_pedido.json")
guardar_datos(pedidos, "pedidos.json")