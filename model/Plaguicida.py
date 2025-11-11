from model.ProductoControl import ProductoControl

class Plaguicida(ProductoControl):
    def __init__(self, ICA: str, nombre: str, frecuencia_aplicacion_dias: int, precio: int, periodo_carencia_dias: int):
                 super().__init__(ICA, nombre, frecuencia_aplicacion_dias, precio)
                 self.periodo_carencia_dias = periodo_carencia_dias
                 

