from abc import ABC, abstractmethod


class IAnimal(ABC):
    # Todos los métodos son abstractos
    @abstractmethod
    def comer(self, kilos: float) -> None:
        """ Método para comer

        Args:
            kilos (float): Kilos comidos por el animal
        """
        pass

    @abstractmethod
    def obtener_kilos_comidos() -> float:
        """ Obtiene los kilos comidos

        Returns:
            float: Cantidad de kilos comidos
        """
        pass
