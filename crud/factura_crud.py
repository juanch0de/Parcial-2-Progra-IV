from modelo.Factura import Factura
from datetime import date

facturas = []
_id_factura = 1

def crear_factura(fecha: date, id_cliente: int) -> Factura:
    global _id_factura
    factura = Factura(fecha,id_cliente)
    factura.id_factura = _id_factura
    _id_factura += 1

    facturas.append(factura)
    return factura

def actualizar_factura(id_factura: int, **datos) -> bool:
    for factura in facturas:
        if getattr(factura, "id_factura", None) == id_factura:
            for atributo, valor in datos.items():
                if hasattr(factura, atributo):
                    setattr(factura, atributo, valor)
            return True
    return False

def eliminar_factura(id_factura: int) -> bool:
    global facturas
    for factura in facturas:
        if getattr(factura, "id_factura", None) == id_factura:
            facturas.remove(factura)
            return True
    return False

def mostrar_facturas() -> list:
    return facturas
