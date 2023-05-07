from mplan import ManejadorPlan
from plan import PlanAhorro
if __name__ == '__main__':
    m=ManejadorPlan()
    m.CargarLista()
    s=int(input('---Menu---\n1.Actualizar el valor del vehiculo de cada plan\n2.Mostrar vehiculos con cuota menor a un precio n\n3.Mostrar monto a pagar para licitar c/vehiculo\n4.Modificar cantidad de cuotas para licitar\nIngrese opcion, cualquier otro numero para finalizar:'))
    while s==1 or s==2 or s==3 or s==4:
        match s:
            case 1:
                m.ActualizarValor()
            case 2:
                m.MostrarMenores()
            case 3:
                m.Licitar()
            case 4:
                PlanAhorro.ModificarCuotasLicitas()
        s=int(input('---Menu---\n1.Actualizar el valor del vehiculo de cada plan\n2.Mostrar vehiculos con cuota menor a un precio n\n3.Mostrar monto a pagar para licitar c/vehiculo\n4.Modificar cantidad de cuotas para licitar\nIngrese opcion, cualquier otro numero para finalizar:'))