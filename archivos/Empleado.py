class Empleado_agregar:
    def __init__(self,idEmpleado,Nombre,Direccion):
        self.idEmpleado = idEmpleado
        self.Nombre = Nombre
        self.Direccion = Direccion 

    def Empleado(self):
        archivo = open("./archivos/empleados.txt","a",encoding="utf8")
        idempleado = input("ID EMPLEADO: \n")
        print("NOMBRE DEL EMPLEADO: ")
        nombre = input("")
        print("DIRECCION:")
        direccion = input("")
        archivo.write(idempleado + "|" + nombre + "|" + direccion + "\n")
        archivo.close()
    

    def consultar_empleado(self):
        archivo = open("./archivos/empleados.txt",encoding="utf8")
        print(archivo.read())

    
    def eliminar_empleado(self):
        archivo = open("./archivos/empleados.txt","a",encoding="utf8")
        idempleado = input("ID EMPLEADO: \n")
        print("NOMBRE DEL EMPLEADO: ")
        nombre = input("")
        print("DIRECCION:")
        direccion = input("")
        archivo.(idempleado,nombre,direccion)
        archivo.close