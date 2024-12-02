from models.animal_exotico import Animal_Exotico


class Huron(Animal_Exotico):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str,
                 impuestos: float) -> None:
        """Constructor de la clase

        Args:
            nombre (str): Nombre del hurón
            edad (int): Edad del hurón
            peso (float): Peso dele hurón
            pais_origen (str): Pais origen del hurón
            impuestos (float): Impuestos del hurón
        """
        super().__init__(nombre, edad, peso, pais_origen, impuestos)

    def hacer_sonido(self):
        """Permite hacer el sonido

        Returns:
            str: Sonido del hurón
        """
        return "¡Eek, Eek!"
