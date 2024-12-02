from models.animal import Animal


class Animal_Exotico(Animal):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str,
                 impuestos: float) -> None:
        """Constructor de la clase

        Args:
            pais_origen (str): Pais origen del animal
            impuestos (float): Valor impuestos del animal
        """
        super().__init__(nombre, edad, peso)

        self._pais_origen = pais_origen
        self._impuestos = impuestos

    def calcular_flete(self, impuestos: float, peso: float) -> float:
        """Calcular el costo de importar un animal

        Args:
            impuestos (float): Valor impuestos
            peso (float): Peso del animal

        Returns:
            float: Costo de importar el animal
        """
        return (impuestos * peso)
