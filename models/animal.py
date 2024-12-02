from abc import abstractmethod
from models.ianimal import IAnimal
from marshmallow import schema, fields


class Animal(IAnimal):

    def __init__(self, nombre: str, edad: int, peso: float) -> None:
        """
        Constructor de la clase
        Args:
            nombre (str): nombre del animal
            edad (int): edad del animal
            peso (float): peso del animal
        """
        self._nombre = nombre
        self._edad = edad
        self._peso = peso
        self.kilos_comidos = 0

    # Métodos
    def comer(self, kilos: float) -> None:
        """Método para comer

        Args:
            kilos (float): Kilos comidos por el animal
        """
        self.kilos_comidos += kilos

    def obtener_kilos_comidos(self) -> float:
        """Obtiene los kilos comidos

        Returns:
            float: Cantidad de kilos comidos
        """
        return self.kilos_comidos

    @abstractmethod
    def hacer_sonido():
        """Método abstracto para hacer sonido
        """
        pass

    def obtener_nombre(self):
        """Obtiene el nombre del animal

        Returns:
            str: Nombre del animal
        """
        return self._nombre

    def obtener_peso(self):
        """Obtiene el peso del animal

        Returns:
            float: Peso del animal
        """
        return self._peso

    def obtener_edad(self):
        """Obtiene la edad del animal

        Returns:
            int: Edad del animal
        """
        return self._edad

    @property
    def nombre(self) -> str:
        """ Devuelve el valor del atributo privado 'nombre' """
        return self._nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'nombre'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self._nombre = value
        else:
            raise ValueError('Expected str')
        
    @property
    def edad(self) -> int:
        """ Devuelve el valor del atributo privado 'edad' """
        return self._edad
    
    @edad.setter
    def edad(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'edad'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self._edad = value
        else:
            raise ValueError('Expected int')
        
    @property
    def peso(self) -> float:
        """ Devuelve el valor del atributo privado 'peso' """
        return self._peso
    
    @peso.setter
    def peso(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'peso'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self._peso = value
        else:
            raise ValueError('Expected float')
