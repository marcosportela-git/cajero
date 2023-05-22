print("Bienvenido a Cajero.")

# Entrada. Datos del usuario.
for i in range(3):
    usuario = str(input("Ingrese su usuario: ")).lower()
    password = str(input("Ingrese su clave: "))

    if usuario == "admin" and password == "1234":
        print("Ingreso exitoso.")
        break
    elif i < 2:
        print("Usuario o clave incorrectos. Intente nuevamente.")
    else:
        print("Cuenta bloqueada.")
        exit()

dinero_base = 10000
total_dinero = dinero_base

# Procesos. Resultados. Menu con salida.
for i in range(9):
    menu = int(input("1) Ingreso de dinero\n2) Extracción de dinero\n3) Consulta de saldo\n4) Salir\nIngrese su selección: "))

    if menu == 1:
        ingreso = float(input("Usted ha seleccionado la opción 1\nIngrese el monto de dinero a ingresar: $ "))
        total_dinero += ingreso
        print("Ingreso exitoso.")
    elif menu == 2:
        extraccion = float(input("Usted ha seleccionado la opción 2\nIngrese el monto de dinero a extraer: $ "))
        if extraccion > total_dinero:
            print("No cuenta con fondos suficientes.")
        else:
            total_dinero -= extraccion
            print("Extracción exitosa.")
    elif menu == 3:
        print("Usted ha seleccionado la opción 3\nSu saldo actual es de $", round(total_dinero, 2))
    elif menu == 4:
        print("*" * 30)
        print("Usted ha seleccionado salir del programa. Saludos.")
        print("*" * 30)
        exit()
    else:
        print("Opción incorrecta. Intente nuevamente.")
