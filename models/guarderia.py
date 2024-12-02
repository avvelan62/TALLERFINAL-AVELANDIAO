from models.boa_constricutor import Boa_Constrictor
from models.huron import Huron

class Guarderia:
    """Constructor de la clase
    """
    def __init__(self, boas: list[Boa_Constrictor], hurones: list[Huron]) -> None:
        self.boas = boas
        self.hurones = hurones
    
    
    """Permite alimentar a las boas

        Args:
            cantidad_raton (int): Cantidad ratones a comer
        Returns:
            str: Resultado de la operación
    """
    def alimentar_boa(self, boa: Boa_Constrictor, cantidad_ratones: int) -> str:
        try:
            if boa is None:
                return "¡Esta Boa no existe!"
            
            boa.comer_raton(cantidad_ratones)
            return "Éxito"
        
        except ValueError as e:
            if "Demasiados Ratones" in e.args[0]:
                return "La boa está llena"
            return str(e)

# Se crean dos boas
boa1 = Boa_Constrictor("Boa 1", 5, 15.0, "Brasil", 100.0)
boa2 = Boa_Constrictor("Boa 2", 3, 12.5, "Colombia", 80.0)

# Se crean dos hurones
huron_1 = Huron("Crash", 2, 2.1, "Uruguay", 12.2)
huron_2 = Huron("Eddy", 2, 1.9, "Uruguay", 12.1)

guarderia = Guarderia([boa1, boa2], [huron_1, huron_2])

# Prueba con resultado: "Éxito"
resultado1 = guarderia.alimentar_boa(guarderia.boas[0], 5)
print(resultado1)  

# Prueba con resultado: "La boa está llena"
resultado2 = guarderia.alimentar_boa(guarderia.boas[1], 15)
print(resultado2) 

# Prueba con resultado: "¡Esta Boa no existe!"
resultado3 = guarderia.alimentar_boa(None, 5)
print(resultado3)