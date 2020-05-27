from Empleado import agregar_Empleado

print ("*"* 30)
print ("Te mostrare el menu inicial")
print ("teclea el numero de la opcion donde deseas hacer un cambio")
opcionInicial =  int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n: "))

if opcionInicial == 1: 
    while opcionInicial == 1:
        print ("elegiste EMPLEADOS") 
        print ("este es el menu disponible: ")
        segundaOpcion = int(input("1. Agregar \n2. Borrar \n3. Modificar \n4. Ver Todo \n5. Ver Empleado Especifico \n:"))
        if segundaOpcion == 1: 
            print ("A continuacion de pedire algunos datos requeridos para agregar empleados:")
            idEmpleado ="\n"
            nombre ="\n"
            direccion = "\n"
            nuevoEmpleado1 = agregar_Empleado(idEmpleado, nombre, direccion)
            nuevoEmpleado1.Agregar_Empleado()
            print ("Tu empleado a sido agregado")
            print ("te mostrare el menu inicial. \nElige una opcion" )
            opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:"))
        elif segundaOpcion == 4: 
            print ("Se te mostrara toda la informacion en la base de datos ")
            archivo = open("./archivos/Empleado.txt",'r')
            print(archivo.read())
            archivo.close()
            print ("se te mostro la informacion requerida")
            print ("*" * 30 )
            final = int (input("te gustaria continuar? 1. SI \n2. NO : "))
            if final == 1: 
                print ("te mostrare el menu inicial. \nElige una opcion" )
                opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:")) 
            elif final ==2: 
                print ("*" * 30 )
                print ("PROGRAMA TERMINADO")
                print ("*" * 30 )
