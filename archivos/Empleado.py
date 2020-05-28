class Empleado_agregar:
    def __init__(self,idEmpleado,Nombre,Direccion):
        self.__idEmpleado = idEmpleado
        self.__Nombre = Nombre
        self.__Direccion = Direccion 
    

    @property
    def idEmpleado (self):
        return self.__idEmpleado
    
    @idEmpleado.setter
    def idEmpleado(self,valor):
        self.__idEmpleado=valor
   
    @property
    def Nombre (self):
        return self.__Nombre
    
    @Nombre.setter
    def Nombre(self,valor):
        self.__Nombre=valor

    @property
    def Direccion (self):
        return self.__Direccion
    
    @Direccion.setter
    def Direccion(self,valor):
        self.__Direccion=valor


    def Empleado(self):
        archivo = open("./archivos/empleados.txt","a",encoding="utf8")
        archivo.write(self.__idEmpleado + "|" + self.__Nombre + "|" + self.__Direccion + "\n")
        archivo.close()
    

    def consultar_empleado(self):
        archivo = open("./archivos/empleados.txt","r",encoding="utf8")
        print(archivo.read())

    
    def eliminar_empleado(self):
        archivo = open("./archivos/empleados.txt","r",encoding="utf8")
        chain = archivo.read()
        chain = chain.replace(self.__idEmpleado + "|" + self.__Nombre + "|" + self.__Direccion,"")    
        archivo.close()   
        otro = open("./archivos/empleados.txt","w",encoding="utf8")    
        otro.write(chain)    
        otro.close()   


    def actualizar_empleado(self):
        archivo = open("./archivos/empleados.txt","r",encoding="utf8")
        chain = archivo.read()
        chain = chain.replace(self.__idEmpleado + "|" + self.__Nombre + "|" + self.__Direccion,"")    
        archivo.close()   
        otro = open("./archivos/empleados.txt","w",encoding="utf8")    
        otro.write(chain)    
        otro.close() 
        archivo = open("./archivos/empleados.txt","r",encoding="utf8")
        chain = archivo.read()
        chain = chain.replace("",self.__idEmpleado + "|" + self.__Nombre + "|" + self.__Direccion)    
        archivo.close() 