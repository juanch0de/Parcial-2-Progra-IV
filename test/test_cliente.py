import unittest
from crud.cliente_crud import crear_cliente, actualizar_cliente, eliminar_cliente, mostrar_clientes

class TestClienteCRUD(unittest.TestCase):
    def setUp(self):
        from crud import cliente_crud
        cliente_crud.clientes.clear()

    def test_crear_cliente(self):
        cliente = crear_cliente("Juan", 1137059159)
        self.assertEqual(cliente.nombre, "Juan")
        self.assertEqual(cliente.ID, 1137059159)
        self.assertEqual(len(mostrar_clientes()), 1)

    def test_actualizar_cliente(self):
        crear_cliente("Juan", 1137059159)
        resultado = actualizar_cliente(1137059159, "Juan Pablo Henao Arias")
        self.assertTrue(resultado)
        self.assertEqual(mostrar_clientes()[0].nombre, "Juan Pablo Henao Arias")

    def test_eliminar_cliente(self):
        crear_cliente("Juan", 1137059159)
        resultado = eliminar_cliente(1137059159)
        self.assertTrue(resultado)
        self.assertEqual(len(mostrar_clientes()), 0)
