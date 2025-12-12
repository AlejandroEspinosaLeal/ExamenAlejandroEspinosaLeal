from espacio import espacio
from apartamento import apartamento
from casa_rural import casaRural
from agencia import agencia
from cliente import cliente


espacio_apt = espacio("Salón", 22.5, True)
apartamento = apartamento("APT-01", "Calle Mayor 10", "Madrid", 80.0, espacio_apt, 3, True)

espacio_casa = espacio("Estudio", 18.0, True)
casa_rural = casaRural("RUR-99", "Camino del Bosque s/n", "Asturias", 120.0, espacio_casa, 200, True)

mi_agencia = agencia("Viajes Felices", "contacto@viajesfelices.com")
mi_agencia.agregar_alojamiento(apartamento)
mi_agencia.agregar_alojamiento(casa_rural)

cliente = cliente("Alejandro Espinosa Leal", "12345678X", "600112233")
cliente.mostrar_info()
print("\nRealizando primera reserva")
cliente.reservar(apartamento)
    
cliente.mostrar_reserva()
    
print("\nCambiando reserva")
cliente.reservar(casa_rural)
cliente.mostrar_reserva()

print("\nActualización de precios")

apartamento.cambiar_precio(95.50)

casa_rural.aumentar_precio_porcentaje(10)


mi_agencia.mostrar_info()

print("\nGestión de Agencia: Quitando alojamiento")
mi_agencia.quitar_alojamiento("APT-01")
mi_agencia.mostrar_info()
