from model.ProductoControl import ProductoControl 
from model.Antibiotico import Antibiotico
from datetime import date

class Factura():
    def __init__(self, fecha: date, id_cliente: int):
        self.fecha = fecha
        self.id_cliente = id_cliente
        self.productos = {}
        self.valor_total = 0


    def agregar_producto_control(self, producto: ProductoControl):
        if producto in self.productos:
            self.productos[producto] += 1
        else:
            self.productos[producto] = 1

    def agregar_antibiotico(self, antibiotico: Antibiotico):
        self.agregar_producto(antibiotico)

    def mostrar_productos(self):
        for producto, cantidad in self.productos.items():
            print(f"{producto.nombre} x {cantidad}")

    def calcular_total(self):
        self.valor_total = sum(producto.precio * cantidad for producto, cantidad in self.productos.items())
        return self.valor_total

    

