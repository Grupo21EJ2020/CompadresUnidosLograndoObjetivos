class Info_Empleado:
    def __init__(self,idEmpleado,Nombre,Direccion):
        self.idEmpleado = idEmpleado
        self.Nombre = Nombre
        self.Direccion = Direccion 

    def AgregarEmpleado():
        print("Agregar un empelado")
        archivo = open("./archivos/empleados.txt","a",encoding="utf8")

        print("Clave del Empleado Nuevo")
        Idempleado = input("Id \n")
        print("Nombre del Empleado:\n")
        Nombre = input("Nombre: \n")
        print("Direccion del Empleado")
        Direccion_Empleado = input("> ")
        archivo.write(idempleado + "|" + nombre + "|" + direccion)
        archivo.close()


    def consultar_empleado():
        archivo = open("./archivos/empleados.txt",encoding="utf8")
        print(archivo.read())