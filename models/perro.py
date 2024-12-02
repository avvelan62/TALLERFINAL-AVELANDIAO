
from models.animal import Animal


class Perro(Animal):
    def __init__(self, nombre: str, edad: int, peso: float) -> None:
        """Constructor de la clase

        Args:
            nombre (str): Nombre del perro
            edad (int): Edad del perro
            peso (float): Peso del perro
        """
        super().__init__(nombre, edad, peso)
        
    def hacer_sonido(self):
        """Permite hacer el sonido

        Returns:
            str: Sonido del perro
        """
        return "¡Guau, Guau!"
