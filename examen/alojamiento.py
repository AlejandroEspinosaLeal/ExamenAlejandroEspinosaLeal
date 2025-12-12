from espacio import espacio

class alojamiento:
    def __init__(self,codigo,direccion,ciudad,precio_por_noche,espacio_principal):
        self.codigo=codigo
        self.direccion=direccion
        self.ciudad=ciudad
        self.precio_por_noche=float(precio_por_noche)
        self.espacio_principal = espacio_principal
    
    def mostrar_info(self):
        print(f"alojamiento {self.codigo}")
        print(f"ubicacion : {self.direccion} , {self.ciudad}")
        print(f"precio : {self.precio_por_noche:.2f} noche")
        print("detalle espacio principal: ")
        self.espacio_principal.mostrar_info()
    
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio>0:
            self.precio_por_noche=float(nuevo_precio)
            print(f"nuevo  precio actualizado a {self.precio_por_noche:.2f}")
        else:
            print("Ell precio tiene que ser mayor a 0")
    def aumentar_precio_porcentaje(self,porcentaje):
        if porcentaje >=0:
            aumento=self.precio_por_noche*(porcentaje/100)
            self.precio_por_noche += aumento
            print(f"precio aumentado un {porcentaje}.nuevo precio:{self.precio_por_noche:.2f}")
        else:
            print("el porcentaje debe ser mayor o igual a 0")
    def get_precio(self):
        return self.precio_por_noche