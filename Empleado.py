class Empleado:
    def __init__(self,idEmpleado,Nombre,Direccion):
        self.idEmpleado = idEmpleado
        self.Nombre = Nombre
        self.Direccion = Direccion 

    def AgregarEmpleado():
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


    def consultar_empleado():
        archivo = open("./archivos/empleados.txt",encoding="utf8")
        print(archivo.read())




    def Actualizar_Contactos(self):
        Nombre = input("Inserta el nombre que quieres buscar: ")
        No_Encontrado = True
        for elemento in self.lista:
            separar = elemento.split('/')
            if Nombre in separar[0]:
                print("Nombre: " + separar[0])
                print("idEmpleado: " + separar[1])
                print("Direccion: " + separar[2])
                print("************************")
            No_Encontrado = False 
        if No_Encontrado == True: 
            print("Contacto no encontrado ")


    def eliminar(self):
        Nombre = input("Inserta el contacto  que quieres eliminar:")
        No_Encontrado = True
        for elemento in self.lista:
            separar = elemento.split('/')
            if Nombre in separar[0]:
                self.lista.remove(elemento)
                No_Encontrado = False
        if No_Encontrado == True:
            print("Contacto no No_Encontrado")
