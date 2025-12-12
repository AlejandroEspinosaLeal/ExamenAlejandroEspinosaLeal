from alojamiento import alojamiento

class casaRural(alojamiento):
    def __init__(self, codigo, direccion,ciudad,precio_por_noche, espacio_principal, metros_jardin, chimenea):
        super().__init__(codigo,direccion,ciudad,precio_por_noche,espacio_principal)
        self.metros_jardin=metros_jardin
        self.chimenea = chimenea

    def mostrar_info(self):
        super().mostrar_info()
        tiene_chimenea = "si" if self.chimenea else "no"
        print(f"tipo: casa rural jardin: {self.metros_jardin}m2  chimenea: {tiene_chimenea}")