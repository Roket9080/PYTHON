from datetime import datetime
import os
cuentas=[]
clientes=[]


def crearCliente():
    os.system('cls')
    identificacion = input("Ingrese Identifiacion Cliente:")
    existeCliente=False
    for cliente in clientes:
        if cliente ['identificacion']==identificacion:
            existeCliente=True
            break
    
    if existeCliente==False:
        #Puedo crear el cliente
        nombre=input("Ingrese nombre del Cliente:")
        correo = input("Ingrese correo del Cliente:")    
        cliente = {
            'identificacion': identificacion,
            'nombre': nombre,
            'correo': correo
        }
        
        clientes.append(cliente) #agregando cliente a la lista
        return identificacion
    else:
        print("Ya exuste cliente con esa identifiacion")
        return


def crearCuenta():
    os.system('cls')
    print("CREACION DE CUENTA")
   
    
    
    #crear cliente si no existe
    identificacionCliente = crearCliente()
    #crear datos cuenta
    fechaHoy= datetime.now()
    yearNow = datetime.now().year
    consecutivo = len(cuentas) + 1 
    codigoCuenta = f"{yearNow}-{consecutivo}"
    saldo = float(input("Ingrese saldo inicial:"))
    
    cuenta = {
        'codigoCuenta': codigoCuenta,
        'saldo': saldo,
        'fechaApertura':fechaHoy,
        'cliente':identificacionCliente
    }
    
    cuentas.append(cuenta)
    


def consignar():
    os.system('cls')
    print("CONSIGNAR")
    codigoCuentaAConsignar = input ("Ingrese codigo de cuenta a Consignar:")
    for cuenta in cuentas:
        if cuenta['codigoCuenta']==codigoCuentaAConsignar:
            valorAConsignar = float(input("Ingrese valor a consignar:"))
            cuenta['saldo'] += valorAConsignar
            print("Consignacion Exitosa")
    else:
        print("No existe cuenta con ese codigo")
    

def retirar():
    pass


def consultarCuentaPorCodigo():
    pass


def consultarPorIdentifacionCliente():
    pass


def listaCuentas():
    os.system('cls')
    print("LISTADO DE CUENTAS")
    print(cuentas)



def menu():
    os.system('cls')
    opcion=0
    while(True):
        print("\t\tMenu banco Adso 3229426")
        print("\t1.Crear Cuenta")
        print("\t2.Consignar")
        print("\t3.Retirar")
        print("\t4.Consultar cuenta X Codigo")
        print("\t5.Consultar cuenta X Identifacion Cliente")
        print("\t6.Listar cuentas")
        print("\t7.Salir")
        opcion = int(input("Ingrese opcion (1-7):"))
        match opcion:
            case 1: crearCuenta()
            case 2: consignar()
            case 3: retirar()
            case 4: consultarCuentaPorCodigo()
            case 5: consultarPorIdentifacionCliente()
            case 6: listaCuentas()
            case 7: 
                print("va a salir")
                break
            case _:print("Opcion no valida")
            
        input("Presione Enter para continuar")








menu()