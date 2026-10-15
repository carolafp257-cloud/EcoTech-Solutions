from clases import Empleado, Cliente, Producto, Pedido

# Datos de prueba para verificar que las clases funcionan bien

empleado1 = Empleado("Maria Perez", "maria@ecotech.cl", "Analista", 650000)
cliente1 = Cliente("Juan Soto", "juan@correo.cl", "Constructora ABC")
producto1 = Producto("P001", "Panel solar", 150000, 20)

print("Datos del empleado:")
empleado1.mostrar_datos()

print("")
print("Datos del cliente:")
cliente1.mostrar_datos()

print("")
print("Datos del producto:")
producto1.mostrar_datos()

# Se genera un pedido para probar la relacion entre las clases
pedido1 = Pedido(cliente1, producto1, 3)

print("")
print("Resumen del pedido:")
pedido1.mostrar_resumen()

# Se verifica que el pedido ya actualiza el stock
print("")
print("Stock despues de la venta:", producto1.obtener_stock())
