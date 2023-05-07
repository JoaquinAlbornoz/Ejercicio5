class PlanAhorro:
    __cantcuotas= 60
    __cuotlicitas= 10

    def __init__(self, cod, mod, ver, p):
        self.__codigo = cod
        self.__modelo = mod
        self.__version = ver
        self.__precio = p
        self.__importecuota = (self.__precio/self.__cantcuotas) + self.__precio * 0.10
    def __lt__(self,n):
        return self.__importecuota<n
    def getprecio(self):
        return self.__precio
    def getValorCuota(self):
        return self.__importecuota
    def MostrarVehiculo(self):
        print(f"{self.__codigo}, {self.__modelo} {self.__version}\n")
    def ActualizarPrecio(self):
        print(f"Codigo de plan: {self.__codigo}, Vehiculo: {self.__modelo} {self.__version}\n")
        self.__precio = float(input( "Ingrese el valor actualizado del vehículo: "))
        print("Valor del vehículo actualizado.")
    def Montolic(self):
        print(f'Vehiculo: {self.__modelo}   Monto a Pagar:{self.__importecuota*self.__cuotlicitas}\n')
    @classmethod
    def ModificarCuotasLicitas(cls):
        print("Modificación de cuotas licitas para pagar un Plan de Ahorro: ")
        x=float(input("Ingrese la nueva cantidad de cuotas licitas de los planes de ahorro: "))
        cls.__cuotlicitas=x
        print ("Se modificó la cantidad de cuotas licitas para todos los planes")