class Curso_agregar:
    def __init__(self,idcurso,Descripcion,Id_empleado):
        self.__idcurso = idcurso
        self.__Descripcion=Descripcion
        self.__Id_empleado =Id_empleado 
    

    @property
    def idcurso (self):
        return self.__idcurso
    
    @idcurso.setter
    def idcurso(self,valor):
        self.__idcurso=valor
   
    @property
    def Descripcion (self):
        return self.__Descripcion
    
    @Descripcion.setter
    def Descripcion(self,valor):
        self.__Descripcion=valor

    @property
    def Id_empleado(self):
        return self.__Id_empleado
    
    @Id_empleado.setter
    def Id_empleado(self,valor):
        self.__Id_empleado=valor


    def Empleado(self):
        archivo = open("./archivos/curso.txt","a",encoding="utf8")
        archivo.write(self.__idcurso + "|" + self.__Descripcion + "|" + self.__Id_empleado + "\n")
        archivo.close()
    

    def consultar_empleado(self):
        archivo = open("./archivos/curso.txt","r",encoding="utf8")
        print(archivo.read())

    
    def eliminar_empleado(self):
        f = open("./archivos/curso.txt","r",encoding="utf8")
        chain = f.read() 
        chain = chain.replace(self.__idcurso + "|" + self.__Descripcion + "|" + self.__Id_empleado,"")    
        f.close()   
        otro = open("./archivos/curso.txt","w",encoding="utf8")    
        otro.write(chain)    
        otro.close()   