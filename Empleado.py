class Empleado:
    def __init__(self,idEmpleado,Nombre,Direccion):
        self.idEmpleado = idEmpleado
        self.Nombre = Nombre
        self.Direccion = Direccion 

    def AgregarEmpleado(self):
        print ("Registro de Empleado")
        archivo = open("./archivos/empleados.txt","a",encoding="utf8")

        print("Clave del Empleado Nuevo")
        idempleado = input("Id \n")
        print("Nombre del Empleado:\n")
        nombre = input("Nombre: \n")
        print("Direccion del Empleado")
        direccion = input("> ")

        archivo.write(idempleado + "|" + nombre + "|" + direccion)
        archivo.close()


    def consultar_empleado(self):
        archivo = open("./archivos/empleados.txt",encoding="utf8")
        print(archivo.read())
