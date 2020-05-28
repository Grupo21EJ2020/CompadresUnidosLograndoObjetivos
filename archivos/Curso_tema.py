class Tema:
    def __init__(self,idCursoTema,idCurso,idTema):
        self.__idcursoTema =idCursoTema
        self.__idCurso=idCurso
        self.__idTema =idTema 
    

    @property
    def idcursoTema (self):
        return self.__idcursoTema
    
    @idcursoTema.setter
    def idcursoTema(self,valor):
        self.__idcursoTema=valor
   
    @property
    def idCurso (self):
        return self.__idCurso
    
    @idCurso.setter
    def idcurso(self,valor):
        self.__idCurso=valor

    @property
    def idTema(self):
        return self.__idTema
    
    @idTema.setter
    def idTema(self,valor):
        self.__idTema=valor


    def curso_tema(self):
        archivo = open("./archivos/Curso_Tema.txt","a",encoding="utf8")
        archivo.write(self.__idcursoTema + "|" + self.__idCurso + "|" + self.__idTema + "\n")
        archivo.close()
    

    def consultar_curso_tema(self):
        archivo = open("./archivos/Curso_Tema.txt","r",encoding="utf8")
        print(archivo.read())

    
    def eliminar_curso_tema(self):
        f = open("./archivos/Curso_Tema.txt","r",encoding="utf8")
        chain = f.read() 
        chain = chain.replace(self.__idcursoTema + "|" + self.__idCurso + "|" + self.__idTema,"")    
        f.close()   
        otro = open("./archivos/Curso_Tema.txt","w",encoding="utf8")    
        otro.write(chain)    
        otro.close()   