#Estructura Match

dia= 2
match dia:
    case 1: print(Lunes)
    case 2: print("Martes")
    case 3: print("Miercoles")
    case 4: print("Jueves")
    case 5: print("Viernes")
    case 6: print("Sabado")
    case 7: print("Domingo")
    case _:print("Dia no existe")
    
mes = 4
match mes:
    case 1|3|5|7|8|10|12:
        print("Mes tiene 31 dias")
    case 2:
        print("Mes tiene 28 o 29 dias")
    case 4|6|9|11:
        print("Mes tiene 30 dias")
    case _: print("Mes no identificado")
  