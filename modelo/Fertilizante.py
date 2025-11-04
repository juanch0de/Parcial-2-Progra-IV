from modelo.ProductoControl import ProductoControl
from datetime import date 

class Fertilizante(ProductoControl):
    def __init__(self, ICA: str, nombre: str, frecuencia_aplicacion_dias: int, precio: int, fecha_ultima_aplicacion: date):
        super().__init__(ICA, nombre, frecuencia_aplicacion_dias, precio)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion

    

