informacion = {}

#Funciones de la gestion:
def ingresar(diccionario):
    try:
        dni = int(input("Ingrese el nuevo dni o 0 para volver:\n"))
        while dni in diccionario.keys() and dni != 0:
            dni = int(input("dni ya existente. Ingrese el nuevo dni o 0 para volver:\n"))
        if dni != 0:
            nombre = input("Ingrese el nombre:\n")
            edad = int(input("Ingrese la edad:\n"))
            profesion = input("Ingrese la profesion:\n").lower()
            activo = input("Se encuentra activo en la empresa? (S/N)\n").upper()
            while activo not in ["S","N"]:
                activo = input("Error.Se encuentra activo en la empresa? (S/N)\n").upper()
            if activo == "S":
                activo = True
            else:
                activo = False
            diccionario[dni] = [nombre,edad,profesion,activo]
    except:
        print("Error. Vuelva a intentar.")
   
def modificar(dni,diccionario):
    while True:
        try:
            opcion = int(input('''Menu de modificar. Que quiere modificar?:
            1- DNI
            2- Nombre
            3- Edad
            4- Profesion
            5- Salir
            '''))
            while opcion not in [1,2,3,4,5]:
                    opcion = int(input("Valor incorrecto. Intente de nuevo"))
            if opcion == 1:
                nuevodni = int(input("Ingrese el nuevo dni:\n"))
                while nuevodni in diccionario.keys() and nuevodni != 0:
                    nuevodni = int(print("Ya se encuentra. Ingrese el nuevo dni o 0 para salir:\n"))
                if nuevodni != 0:
                    diccionario[nuevodni] = diccionario[dni]
                    diccionario.pop(dni)
                    print("Se modifico correctamente.")
            elif opcion == 2:
                nombree = input(f"Ingrese el nuevo nombre para el dni {dni}\n")
                diccionario[dni][0] = nombree
                print("Cambio exitoso!")
            elif opcion == 3:
                eedad = int(input(f"Ingrese la nueva edad para el dni {dni}\n"))
                diccionario[dni][1] = eedad
                print("Cambio exitoso!")
            elif opcion == 4:
                profesioon = input(f"Ingrese la nueva profesion del dni {dni}\n")
                diccionario[dni][2] = profesioon
            else:
                break
        except:
            print("Error.")

def eliminar(dni,diccionario):
    diccionario.pop(dni)
    print("Se elimino correctamente.")

#Funciones de los reportes:
def activos(diccionario):
    print("Trabajadores activos:")
    for x,i in diccionario.items():
        if i[3] == True:
            print(f"DNI: {x} Nombre: {i[0]} Profesion: {i[2]}")

def desocupados(diccionario):
    print("Trabajadores desocupados:")
    for x,i in diccionario.items():
        if i[3] == False:
            print(f"DNI: {x} Nombre: {i[0]} Profesion: {i[2]}")

def desocupadosRango(diccionario,inicio,fin):
    print("Trabajadores desocupados:")
    for x,i in diccionario.items():
        if i[1] >= inicio and i[1] <= fin:
            if i[3] == False:
                print(f"DNI: {x} Nombre: {i[0]} Profesion: {i[2]}")

def profesion(diccionario):
    trabajo = input("Ingrese la profesion que busca:\n").lower()
    print(f"Trabajadores que son {trabajo}:")
    for x,i in diccionario.items():
        if i[2] == trabajo:
            print(f"DNI: {x} Nombre: {i[0]}")

#Menu gestion
def menuGestion(diccionario):
    while True:
        try:
            opcion = int(input('''Menu de gestion! Ingrese su opción:
            1- Ingresar nuevo trabajador
            2- Modificar informacion de un trabajador
            3- Eliminar trabajador
            4- Volver
            '''))
            while opcion not in [1,2,3,4]:
                opcion = int(input("Valor incorrecto. Intente de nuevo"))
            if opcion == 1:
                ingresar(diccionario)
            elif opcion == 2:
                try:
                    dni = int(input("Ingrese el dni del trabajador que quiere modificar o 0 para salir:\n"))
                    while dni not in diccionario.keys() and dni != 0:
                        dni = int(input("dni incorrecto. Ingrese de nuevo o 0 para salir:\n"))
                    if dni != 0:
                        modificar(dni,diccionario)
                except:
                    print("Valor incorrecto. Intente de nuevo")
            elif opcion == 3:
                try:
                    dni = int(input("Ingrese el dni del trabajador que quiere eliminar o 0 para salir:\n"))
                    while dni not in diccionario.keys() and dni != 0:
                        dni = int(input("dni incorrecto. Ingrese de nuevo o 0 para salir:\n"))
                    if dni != 0:
                        eliminar(dni,diccionario)
                except:
                    print("Valor incorrecto. Intente de nuevo")
            elif opcion == 4:
                break
        except:
            print("Valor incorrecto. Intente de nuevo.")

#Menu reportes
def menuReportes(diccionario):
    while True:
        try:
            opcion = int(input('''Menu de reportes! Ingrese su opción:
            1- Mostrar trabajadores activos
            2- Mostrar trabajadores desocupados
            3- Mostrar desocupados en un rango de edad
            4- Mostrar trabajadores según la profesión que indique
            5- Volver
            '''))
            while opcion not in [1,2,3,4,5]:
                opcion = int(input("Valor incorrecto. Intente de nuevo"))
            if opcion == 1:
                activos(diccionario)
            elif opcion == 2:
                desocupados(diccionario)
            elif opcion == 3:
                try:
                    inicio = int(input("Ingrese el inicio del rango\n"))
                    fin = int(input("Ingrese el final del rango\n"))
                    desocupadosRango(diccionario,inicio,fin)
                except:
                    print("Valor incorrecto. Intente de nuevo")
            elif opcion == 4:
                profesion(diccionario)
            else:
                break
        except:
            print("Valor incorrecto. Intente de nuevo.")

def cambiarEstado(diccionario):
    try:
        dni = int(input("Ingrese el dni del trabajador que quiere modificar su estado:\n"))
        while dni not in diccionario.keys() and dni != 0:
            dni = int(input("dni incorrecto. Ingrese de nuevo o 0 para salir:\n"))
        if dni != 0:
            diccionario[dni][3] = not diccionario[dni][3]
    except:
        print("Valor incorrecto. Intente de nuevo")