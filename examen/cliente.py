class cliente:
    def __init__(self, nombre, dni, telefono):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.alojamiento_actual = None

    def mostrar_info(self):
        print(f"Cliente{self.nombre} (DNI: {self.dni},Tlf: {self.telefono})")

    def reservar(self, alojamiento):
        self.alojamiento_actual = alojamiento
        print(f"reserva realizada con éxito en {alojamiento.codigo} para {self.nombre}.")

    def cancelar_reserva(self):
        self.alojamiento_actual = None
        print(f"Reserva cancelada para {self.nombre}.")

    def mostrar_reserva(self):
        if self.alojamiento_actual:
            print(f"\nReserva actual de {self.nombre}")
            self.alojamiento_actual.mostrar_info()
        else:
            print(f"{self.nombre} no tiene ninguna reserva activa.")