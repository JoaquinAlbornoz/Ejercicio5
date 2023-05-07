from plan import PlanAhorro
import csv

class ManejadorPlan:
    def __init__(self):
        self.__lista=[]
    def CargarLista(self):
        with open('C:\\Users\\users\\Documents\\Cristiannika\\SEGUNDO AÑO DE FACULTAD\\Programacion orientada a objetos\\UNIDAD 2\\Ejercicio 5\\planes.csv', 'r') as f:
            reader= csv.reader(f, delimiter=';')
            for fila in reader:
                if fila[0] != None and fila[1] != None and fila[2] != None and fila[3] != None:
                    obj= PlanAhorro(fila[0],fila[1],fila[2],float(fila[3]))
                    self.__lista.append(obj)
    
    def ActualizarValor(self):
        print("Modificación de valores")
        for i in range(len(self.__lista)):
            self.__lista[i].ActualizarPrecio()

    def MostrarMenores(self):
        print("Mostrar inferiores al valor dado:\n")
        x=float(input("Ingrese el valor: "))
        print("\nLos vehículos que son menores al precio ingresado son los siguientes:\n")
        for i in range(len(self.__lista)):
            if (self.__lista[i] < x):
                self.__lista[i].MostrarVehiculo()
    def Licitar(self):
        for i in range(len(self.__lista)):
            self.__lista[i].Montolic()
