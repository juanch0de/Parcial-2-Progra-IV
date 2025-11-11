from model.ProductoControl import ProductoControl
from enum import StrEnum

class Animal(StrEnum):
    BOVINOS = "bovino"
    CAPRINOS = "caprino"
    PORCINOS = "porcino"


class Antibiotico():
    def __init__(self, nombre: str, dosisKG: int, animal: str, precio: int):
        self.nombre = nombre
        animal = animal.lower()
        self.animal = Animal(animal)
        self.precio = precio
        
        if not (400 <= dosisKG <= 600):
            raise ValueError("La dosis debe estar entre 400 y 600 kg")
        self.dosisKG = dosisKG
