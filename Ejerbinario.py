def decimalABinario(numero):
    respuesta=''
    resultado=numero
    while(True):
        valorInicial=resultado
        residuo= valorInicial % 2
        respuesta += str(residuo)
        resultado = valorInicial //2 
        
        if resultado == 1:
            respuesta += str(resultado)
            break
        
    
    respuesta = "".join(reversed(respuesta))
    
    return respuesta
            
            

numeroEntrada = int(input("Ingrese numero Entero para convertir a Binario: "))

binario = decimalABinario(numeroEntrada)

print(f"El numero {numeroEntrada} en Binario es {binario}")