from modelo.ProductoControl import ProductoControl

class Antibiotico():
    def __init__(self, nombre: str, dosisKG: int, animal: str, precio: int):
        self.nombre = nombre
        self.dosisKG = dosisKG
        self.animal = animal
        self.precio = precio
