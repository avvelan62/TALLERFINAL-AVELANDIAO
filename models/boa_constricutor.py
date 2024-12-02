from models.animal_exotico import Animal_Exotico


class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str,
                 impuestos: float) -> None:
        """Constructor de la clase

        Args:
            nombre (str): Nombre de la boa
            edad (int): Edad de la boa
            peso (float): Peso de la boa
            pais_origen (str): Pais origen de la boa
            impuestos (float): Impuestos de la boa
        """
        super().__init__(nombre, edad, peso, pais_origen, impuestos)
        self._ratones_comidos = 0

    def hacer_sonido(self):
        """Permite hacer el sonido

        Returns:
            str: Sonido de la Boa
        """
        return "¡Tsss!"

    def comer_raton(self, cantidad_raton: int) -> None:
        """Agrega ratones comidos

        Args:
            cantidad_raton (int): Cantidad ratones comidos
        """
        if  cantidad_raton >= 20:
            raise ValueError("¡Demasiados Ratones!")
        
        self._ratones_comidos += cantidad_raton

    def contar_ratones_comidos(self) -> int:
        """Permite contar los ratones comidos

        Returns:
            int: Cantidad de ratones comidos
        """
        return self._ratones_comidos
