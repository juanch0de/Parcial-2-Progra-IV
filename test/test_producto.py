import unittest
from crud.producto_crud import crear_producto, actualizar_productos, eliminar_productos, mostrar_productos
from modelo.Fertilizante import Fertilizante
from modelo.Plaguicida import Plaguicida
from modelo.Antibiotico import Antibiotico
from datetime import date

class TestProductoCRUD(unittest.TestCase):
    def setUp(self):
        global productos
        productos.clear()

    def test_crear_fertilizante(self):
        f = crear_producto(
                "fertilizante",
                ICA ="F001",
                nombre = "Sulfacas",
                frecuencia_aplicacion_dias = 10,
                precio = 50000,
                fecha_ultima_aplicacion = date(2025,11,4)
                )
        self.assertIsInstance(f, Fertilizante)
        self.assertEqual(f.nombre, "Sulfacas")
        self.assertEqual(f.ICA, "F001")
                    
