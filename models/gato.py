
from models.animal import Animal


class Gato(Animal):
    def __init__(self, nombre: str, edad: int, peso: float) -> None:
        """Constructor de la clase

        Args:
            nombre (str): Nombre del gato
            edad (int): Edad del gato
            peso (float): Peso del gato
        """
        super().__init__(nombre, edad, peso)

    def hacer_sonido(self):
        """Permite hacer el sonido

        Returns:
            str: Sonido del gato
        """
        return "¡Miau, Miau!"
