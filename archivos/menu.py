from Empleado import Empleado_agregar
Menu =  int(input("------MENU----\n1.Empleado \n2.Curso \n3.Tema \n4.Video \n: "))
print ("---Elige una Opcion---")

if Menu == 1: 
    while Menu >= 1:
        submenu = int(input("--------SUBMENU------ \n1.Agregar \n2.Borrar \n3.Modificar \n4.Consultar \n5. Ver Empleado Especifico \n:"))
        if submenu == 1: 
            print ("-------DATOS DE EMPLEADOS------")
            idEmpleado=input("Ingresa el ID del empleado\n")
            Nombre =input("Ingresa el nombre del empleado\n")
            Direccion = input("Ingresa la direecion del empleado\n1")
            nuevoEmpleado1 = Empleado_agregar(idEmpleado, Nombre, Direccion)
            nuevoEmpleado1.Empleado()
            print ("----ELEGIR OTRA OPCION----\n" )
            Menu = int(input("1.Empleado \n2.Curso \n3.Tema \n4.Video \n:"))

        if submenu == 2: 
            print ("-------BORRAR EMPLEADOS------\n")
            idEmpleado=input("Ingresa el ID del empleado\n")
            Nombre =input("Ingresa el nombre del empleado\n")
            Direccion = input("Ingresa la direccion del empleado \n")
            eliminarEmpleado1 = Empleado_agregar(idEmpleado,Nombre,Direccion)
            eliminarEmpleado1.eliminar_empleado()
            print ("----ELEGIR OTRA OPCION----\n" )
            Menu = int(input("1.Empleado \n2.Curso \n3.Tema \n4.Video \n:"))
        if submenu == 3: 
            print ("-------D EMPLEADOS------:")
            idEmpleado =""

            nombre =""
            direccion = ""
            print ("----ELEGIR OTRA OPCION----\n" )
            Menu = int(input("1.Empleado \n2.Curso \n3.Tema \n4.Video \n:"))   
        elif submenu == 4:
            print("---------Consulta de Empleados----------\n") 
            print ("----Se te mostrara la informacion de los empleados--- \n")
            archivo = open("./archivos/empleados.txt",encoding="utf8")
            print(archivo.read())
            salir = int (input("---Quieres Continuar??---\n1. SI \n2. NO : "))
            if salir == 1: 
                Menu = int(input("------MENU---- \n1.Empleado \n2.Curso \n3.Tema \n4.Video \n:"))
            elif salir ==2: 
                print("Saliendo....")
                break
                
                
                   
