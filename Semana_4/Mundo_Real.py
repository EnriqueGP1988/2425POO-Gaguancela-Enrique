#  EJEMPLO REALIZADO DE PRODUCTOS DE UNA LIBRERIA

# Creación de la clase "Producto"

class  Producto:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

# Creación de la clase "Pedido"
class Pedido:
    def __init__(self, identificador):
        self.identificador = identificador
        self.productos ={}

    def agregar_producto(self, producto,stock):
        if producto.nombre in self.productos:
            self.productos[producto.nombre]["stock"] += stock
        else:
            self.productos[producto.nombre] = {"producto":producto,"stock":stock}

    def eliminar_producto(self, producto,stock):
        if producto.nombre in self.productos:
            self.productos[producto.nombre]["stock"] -= stock
            if self.productos[producto.nombre]["stock"] <= 0:
                del self.productos[producto.nombre]
    def obtener_total(self):
        total = 0
        for item in self.productos.values():
            total += item["producto"].valor * item["stock"]
        return total

    def mostrar_detalles(self):
        print(f"El usuario {self.identificador} a realizado el siguiente inventario:")
        for nombre, detalle  in self.productos.items():
            producto = detalle["producto"]
            stock = detalle["stock"]
            print(f"{nombre}: Precio unitario $ {producto.valor} y en stock la cantidad de {stock} unidades")
        print(f"Valor total de los artículos: $ {(self.obtener_total())}")


# CREACIÓN DE LOS PRODUCTOS DE LA LIBRERÍA

# Precio de venta al público de los esferos.
producto1 = Producto("Esfero", 0.5)
# Precio de venta al público de los esferos.
producto2 = Producto("Cuaderno", 2)

# Cantidad de productos en bodega.
pedido = Pedido("Enrique")
pedido.agregar_producto(producto1,300)
pedido.agregar_producto(producto2,300)

pedido.mostrar_detalles()

# Número de artículos que se han vendio.
pedido.eliminar_producto(producto1,7)
pedido.eliminar_producto(producto2,20)
pedido.mostrar_detalles()