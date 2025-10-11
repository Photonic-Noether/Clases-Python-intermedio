#Fabrica: sirve para crear clases y añadir atributos que afectan a la clase principal sin añadir nuevos metodos a esta

# Fabrica de Pizzas masa e ingredientes
#pizzas premium con su atributo premium

#from dataclasses import dataclass

#funciones sin return llamadas mudas
def descuento_premium():
    descuento = "Felicidades, tienes un descuento!"
    print(descuento)

class Pizza:
    def __init__(self, masa: str, ingredientes: list[str]):
        self.masa = masa
        self.ingredientes = ingredientes



class FabricaPizzas:
    def crear_pizza(self,masa: str, ingredientes: list[str], premium = False):
        p = Pizza(masa, ingredientes)
        if premium:
            p.premium = True
            p.ganar_descuento = descuento_premium
        return p
    

    

frabrica = FabricaPizzas()

pizza = frabrica.crear_pizza("rellena de queso", ["jamon", "queso", "aceitunas"],premium=True)

print(pizza.masa)
print(pizza.ingredientes)

pizza.ganar_descuento()
