from alojamiento import alojamiento

class apartamento(alojamiento):
    def __init__(self, codigo, direccion, ciudad, precio_por_noche, espacio_principal, numero_planta, ascensor):
        super().__init__(codigo, direccion, ciudad, precio_por_noche, espacio_principal)
        self.numero_planta = numero_planta
        self.ascensor = ascensor

    def mostrar_info(self):
        super().mostrar_info()
        tiene_ascensor = "si" if self.ascensor else "no"
        print(f"Tipo: Apartamento Planta: {self.numero_planta} Ascensor: {tiene_ascensor}")