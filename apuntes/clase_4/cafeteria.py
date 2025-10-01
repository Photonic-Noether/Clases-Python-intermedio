# Requisitos funcionales:
# La cafetería vende productos (café, té, pasteles, etc.).
# Un cliente puede hacer un pedido con uno o varios productos.
# Cada pedido debe calcular su total automáticamente.
# El sistema debe permitir múltiples métodos de pago (efectivo, tarjeta, PayPal, etc.).
# Debe ser fácil añadir nuevos tipos de productos o pagos sin modificar las clases existentes.
# El pedido puede generar un recibo imprimible o en PDF, según se elija.

from abc import ABC, abstractmethod

class Producto():
    def __init__(self, nombre:str, precio:float):
        self.nombre = nombre
        self.precio = precio

class Cliente():
    def __init__(self, nombre:str):
        self.nombre = nombre
    
class MetodoDePago(ABC):
    @abstractmethod
    def pagar(self, cantidad):
        pass

class PagoEfectivo(MetodoDePago):
    def pagar(self, cantidad):
        ...

class PagoTarjeta(MetodoDePago):
    def pagar(self, cantidad):
        ...

class PagoPayPal(MetodoDePago):
    def pagar(self, cantidad):
        ...



    

class Pedido():
    def __init__(self):
        self.lista_productos = []
        self.metodo_pago = None

    def añadirProducto(self, producto:Producto):
        self.lista_productos.append(
            {"producto":producto.nombre, 
             "precio":producto.precio}
            )

    def mostrarProductos(self):
        if not self.lista_productos:
            print("La lista esta vacia")
        else:
            for item in self.lista_productos:
                print(f"{item['producto']} - {item['precio']}€")

    def calcularTotal(self):
        total = 0
        for i in self.lista_productos:
            total = total + i['precio']
        return total
    
    def mostrarTotal(self):
        total = self.calcularTotal()
        print(f"Total del pedido = {total}€")

    def establecerMetodoDePago(self, metodo: MetodoDePago):
        self.metodo_pago = metodo

    



producto1 = Producto("Arroz", 0.89)
producto2 = Producto("Café", 1.50)
producto3 = Producto("Té", 1.20)
producto4 = Producto("Pastel", 2.00)

pedido1 = Pedido()
pedido1.añadirProducto(producto1)
pedido1.añadirProducto(producto2)
pedido1.añadirProducto(producto3)
pedido1.añadirProducto(producto4)
pedido1.mostrarProductos()
pedido1.calcularTotal()
pedido1.mostrarTotal()
pedido1.pagar(5.59)