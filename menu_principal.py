import trabajadores

while True:
    try:
        opcion = int(input('''Bienvenido al menu! Ingrese su opción:
        1- Gestion de trabajadores
        2- Reportes
        3- Cambiar el estado de un trabajador
        0- Salir
        '''))
        while opcion not in [1,2,3,0]:
            opcion = int(input("Error. Ingrese de nuevo la opcion."))
        if opcion == 1:
            trabajadores.menuGestion(trabajadores.informacion)
        elif opcion == 2:
            trabajadores.menuReportes(trabajadores.informacion)
        elif opcion == 3:
            trabajadores.cambiarEstado(trabajadores.informacion)
        else:
            break
    except:
        print("Valor incorrecto. Intente de nuevo.")

for x,i in trabajadores.informacion.items():
    print(f"DNI: {x}\nNOMBRE: {i[0]}\nEDAD: {i[1]}\nPROFESION: {i[2]}")
    if i[3] == True:
        print("Se encuentra activo en la empresa")
    else:
        print("No se encuentra activo en la empresa")
    print("-------------------------------------------")