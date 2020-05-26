
from Empleado import Empleado


class  Menu_:
    def menu(self):

        print(" 1.Empleados")
        print(" 2.")
        print(" 3.Empleados")
        print(" 4.Empleados")
        inicio= 0
        while inicio > 1:
            opcion =int(input("Elige un tema"))
            if opcion == 1:
                return Empleado.AgregarEmpleado
            else:
                print('nojalo')
                    
