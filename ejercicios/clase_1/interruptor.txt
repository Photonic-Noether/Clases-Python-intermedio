class Interruptor:
    def __init__(self):
        self.estado = False  # False = apagado, True = encendido
    
    def encender(self):
        if not self.estado:
            self.estado = True
            print("Interruptor ENCENDIDO")
        else:
            print("El interruptor ya está encendido")
    
    def apagar(self):
        if self.estado:
            self.estado = False
            print("Interruptor APAGADO")
        else:
            print("El interruptor ya está apagado")
    
    def alternar(self):
        """Alterna entre encendido y apagado"""
        self.estado = not self.estado
        if self.estado:
            print("Interruptor ENCENDIDO")
        else:
            print("Interruptor APAGADO")
    
    def mostrar_estado(self):
        estado_texto = "ENCENDIDO" if self.estado else "APAGADO"
        print(f"Estado actual: {estado_texto}")
        return self.estado

# Función principal
def main():
    interruptor = Interruptor()
    
    while True:
        print("\n" + "="*40)
        print("        INTERRUPTOR ELECTRÓNICO")
        print("="*40)
        print("1. Encender")
        print("2. Apagar")
        print("3. Alternar (encender/apagar)")
        print("4. Mostrar estado")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción (1-5): ")
        
        if opcion == "1":
            interruptor.encender()
        elif opcion == "2":
            interruptor.apagar()
        elif opcion == "3":
            interruptor.alternar()
        elif opcion == "4":
            interruptor.mostrar_estado()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()