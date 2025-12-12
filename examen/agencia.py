class agencia:
    def __init__(self,nombre,correo_contacto):
        self.nombre = nombre
        self.correo_contacto=correo_contacto
        self.lista_alojamientos=[]

    def agregar_alojamiento(self, alojamiento):
        self.lista_alojamientos.append(alojamiento)
        print(f"alojamiento {alojamiento.codigo} agregado a la agencia {self.nombre}.")

    def quitar_alojamiento(self, codigo):
        alojamiento_a_borrar = None

        for aloj in self.lista_alojamientos:
            if aloj.codigo == codigo and alojamiento_a_borrar is None:
                alojamiento_a_borrar = aloj

        if alojamiento_a_borrar:
            self.lista_alojamientos.remove(alojamiento_a_borrar)
            print(f"alojamiento {codigo} eliminado de la agencia.")
        else:
            print(f"no se encontró el alojamiento {codigo} en la agencia.")

    def mostrar_info(self):
        print(f"\nagencia: {self.nombre} ({self.correo_contacto})")
        print(f"total alojamientos gestionados: {self.contar_alojamientos()}")
        for aloj in self.lista_alojamientos:
            print("-" * 30)
            aloj.mostrar_info()
        print("=" * 40)

    def contar_alojamientos(self):
        return len(self.lista_alojamientos)