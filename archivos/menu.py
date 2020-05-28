from Empleado import Empleado_agregar
from Curso import Curso_agregar
from Curso_tema import Tema
Menu =  int(input("------MENU----\n1.Empleado \n2.Curso \n3.Tema \n4.Video \n5.Curso_Tema\n "))
print ("---Elige una Opcion---")

if Menu == 1: 
    while Menu >= 1:
        submenu = int(input("--------SUBMENU------ \n1.Agregar \n2.Borrar \n3.Modificar \n4.Consultar\n"))
        if submenu == 1: 
            print ("-------DATOS DE EMPLEADOS------")
            idEmpleado=input("Ingresa el ID del empleado\n")
            Nombre =input("Ingresa el nombre del empleado\n")
            Direccion = input("Ingresa la direecion del empleado\n")
            nuevoEmpleado1 = Empleado_agregar(idEmpleado, Nombre, Direccion)
            nuevoEmpleado1.Empleado()
            print ("----ELEGIR OTRA OPCION----\n" )
            Menu = int(input("1.Empleado \n2.Curso \n3.Tema \n4.Video \n5.Curso_Tema\n"))

        elif submenu == 2: 
            print ("-------BORRAR EMPLEADOS------\n")
            idEmpleado=input("Ingresa el ID del empleado\n")
            Nombre =input("Ingresa el nombre del empleado\n")
            Direccion = input("Ingresa la direccion del empleado \n")
            eliminarEmpleado1 = Empleado_agregar(idEmpleado,Nombre,Direccion)
            eliminarEmpleado1.eliminar_empleado()
            print ("----ELEGIR OTRA OPCION----\n" )
            Menu = int(input("1.Empleado \n2.Curso \n3.Tema \n4.Video \n5.Curso_Tema\n"))
        elif submenu == 3: 
            print ("-------D EMPLEADOS------:")
            idEmpleado=input("")
            Nombre=input("")
            Direccion=input("")
            modificarempleado=Empleado_agregar(idEmpleado,Nombre,Direccion)
            modificarempleado.actualizar_empleado()
            print ("----ELEGIR OTRA OPCION----\n" )
            Menu = int(input("1.Empleado \n2.Curso \n3.Tema \n4.Video \n5.Curso_Tema\n"))   
        elif submenu == 4:
            print("---------Consulta de Empleados----------\n") 
            print ("----Se te mostrara la informacion de los empleados--- \n")
            archivo = open("./archivos/empleados.txt",encoding="utf8")
            print(archivo.read())
            salir = int (input("---Quieres Continuar??---\n1. SI \n2. NO : "))
            if salir == 1: 
                Menu = int(input("------MENU---- \n1.Empleado \n2.Curso \n3.Tema \n4.Video \n5.Curso_Tema\n"))
            elif salir ==2: 
                print("Saliendo....")
                break
elif Menu == 2:
     while Menu >= 1:
        submenu = int(input("--------SUBMENU------ \n1.Agregar \n2.Borrar \n3.Modificar \n4.Consultar\n"))
        if submenu == 1: 
            print ("-------DATOS DE CURSOS------")
            idcurso=input("Ingresa el ID del curso\n")
            Descripcion =input("Ingresa la descripcion del curso\n")
            Id_empleado = input("Ingresa la direccion del empleado\n")
            nuevocurso1 = Curso_agregar(idcurso,Descripcion,Id_empleado)
            nuevocurso1.curso()
            print ("----ELEGIR OTRA OPCION----\n")
            Menu = int(input("1.Empleado \n2.Curso \n3.Tema \n4.Video \n5.Curso_Tema\n"))
        elif submenu == 2: 
            print ("-------BORRAR CURSOS------\n")
            idcurso=input("Ingresa el ID del curso\n")
            Descripcion =input("Ingresa la descripcion del curso\n")
            Id_empleado = input("Ingresa la direccion del empleado\n")
            eliminarcurso1 = Curso_agregar(idcurso,Descripcion,Id_empleado)
            eliminarcurso1.eliminar_curso()
            print ("----ELEGIR OTRA OPCION----\n" )
            Menu = int(input("1.Empleado \n2.Curso \n3.Tema \n4.Video \n5.Curso_Tema\n"))
        elif submenu == 3: 
            print ("-------ACTUALIZAR CURSOS------:")
            idEmpleado=input("")
            Nombre=input("")
            Direccion=input("")
            print ("----ELEGIR OTRA OPCION----\n" )
            Menu = int(input("1.Empleado \n2.Curso \n3.Tema \n4.Video \n5.Curso_Tema\n"))   
        elif submenu == 4:
            print("---------CONSULTA DE CURSOS----------\n") 
            print ("----Se te mostrara la informacion de los cursos--- \n")
            archivo = open("./archivos/curso.txt",encoding="utf8")
            print(archivo.read())
            salir = int (input("---Quieres Continuar??---\n1. SI \n2. NO : "))
            if salir == 1: 
                Menu = int(input("------MENU---- \n1.Empleado \n2.Curso \n3.Tema \n4.Video \n5.Curso_Tema\n"))
            elif salir ==2: 
                print("Saliendo....")
                break               
                
elif Menu == 5:
     while Menu >= 1:
        submenu = int(input("--------SUBMENU------ \n1.Agregar \n2.Borrar \n3.Modificar \n4.Consultar\n"))
        if submenu == 1: 
            print ("-------DATOS DE CURSOS_TEMA------")
            idcursoTema=input("Ingresa el ID del curso_tema\n")
            idcurso =input("Ingresa el id del curso\n")
            idTema = input("Ingresa el id del tema\n")
            nuevotemacurso1 = Tema(idcursoTema,idcurso,idTema)
            nuevotemacurso1.curso_tema()
            print ("----ELEGIR OTRA OPCION----\n" )
            Menu = int(input("1.Empleado \n2.Curso \n3.Tema \n4.Video \n5.Curso_Tema\n"))
        elif submenu == 2: 
            print ("-------BORRAR CURSOS_TEMA------\n")
            idcursoTema=input("Ingresa el ID del curso_tema\n")
            idCurso =input("Ingresa el id del curso\n")
            idTema = input("Ingresa el id del tema\n")
            eliminartemacurso1 = Tema(idcursoTema,idCurso,idTema)
            eliminartemacurso1.eliminar_curso_tema()
            print ("----ELEGIR OTRA OPCION----\n" )
            Menu = int(input("1.Empleado \n2.Curso \n3.Tema \n4.Video \n5.Curso_Tema\n"))
        elif submenu == 3: 
            print ("-------ACTUALIZAR CURSOS_TEMA------:")
            idEmpleado=input("")
            Nombre=input("")
            Direccion=input("")
            print ("----ELEGIR OTRA OPCION----\n" )
            Menu = int(input("1.Empleado \n2.Curso \n3.Tema \n4.Video \n5.Curso_Tema\n"))   
        elif submenu == 4:
            print("---------CONSULTA DE CURSOS_TEMA----------\n") 
            print ("----Se te mostrara la informacion de los cursos--- \n")
            archivo = open("./archivos/Curso_Tema.txt",encoding="utf8")
            print(archivo.read())
            salir = int (input("---Quieres Continuar??---\n1. SI \n2. NO : "))
            if salir == 1: 
                Menu = int(input("------MENU---- \n1.Empleado \n2.Curso \n3.Tema \n4.Video \n5.Curso_Tema\n"))
            elif salir ==2: 
                print("Saliendo....")
                break               
                                  
