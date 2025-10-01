class Deuda:
    """
    Clase que representa una deuda con un titular y un monto.
    Incluye métodos dunder para facilitar su uso como objeto nativo de Python.
    """

    def __init__(self, titular, monto):
        """
        Inicializa una instancia de Deuda.

        Args:
            titular (str): Nombre del titular de la deuda.
            monto (int o float): Monto de la deuda.
        """
        self.titular = titular
        self.monto = monto

    def __str__(self):
        """
        Representación amigable del objeto, útil para mostrar al usuario.

        Returns:
            str: Texto descriptivo de la deuda.
        """
        return f"Deuda de {self.titular}: {self.monto}€"

    def __repr__(self):
        """
        Representación técnica del objeto, útil para depuración.

        Returns:
            str: Cadena que permite reconstruir el objeto.
        """
        return f"Deuda(titular='{self.titular}', monto={self.monto})"

    def __eq__(self, other):
        """
        Compara dos objetos Deuda por igualdad.

        Args:
            other (Deuda): Otro objeto Deuda.

        Returns:
            bool: True si tienen el mismo titular y monto, False en caso contrario.
        """
        return isinstance(other, Deuda) and self.titular == other.titular and self.monto == other.monto

    def __add__(self, other):
        """
        Suma dos objetos Deuda, combinando sus montos si tienen el mismo titular.

        Args:
            other (Deuda): Otro objeto Deuda.

        Returns:
            Deuda: Nueva instancia con el monto combinado.
        """
        if isinstance(other, Deuda):
            return Deuda(self.titular, self.monto + other.monto)
        return NotImplemented

    def __len__(self):
        """
        Devuelve la longitud del monto como número de dígitos.

        Returns:
            int: Cantidad de dígitos del monto.
        """
        return len(str(self.monto))

    def __lt__(self, other):
        """
        Compara si esta deuda es menor que otra según el monto.

        Args:
            other (Deuda): Otro objeto Deuda.

        Returns:
            bool: True si esta deuda tiene menor monto, False en caso contrario.
        """
        return self.monto < other.monto

class Deuda:
  
    def __init__(self, titular, monto):
      
        self.titular = titular
        self.monto = monto

    def __str__(self):
       
        return f"Deuda de {self.titular}: {self.monto}€"

    def __repr__(self):
     
        return f"Deuda(titular='{self.titular}', monto={self.monto})"

    def __eq__(self, other):
      
        return isinstance(other, Deuda) and self.titular == other.titular and self.monto == other.monto

    def __add__(self, other):
       
        if isinstance(other, Deuda):
            return Deuda(self.titular, self.monto + other.monto)
        return NotImplemented

    def __len__(self):
     
        return len(str(self.monto))

    def __lt__(self, other):
    
        return self.monto < other.monto