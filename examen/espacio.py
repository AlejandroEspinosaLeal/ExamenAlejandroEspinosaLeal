class espacio:
    def __init__(self,nombre,metros_cuadrados,ventanas):
        self.nombre=nombre
        self.metros_cuadrados = metros_cuadrados
        self.ventanas = ventanas
    def mostrar_info(self):
        tiene_ventanas="si" if self.ventanas else "no"
        print(f" {self.nombre} : {self.metros_cuadrados}m2 , ventanas:{tiene_ventanas}")