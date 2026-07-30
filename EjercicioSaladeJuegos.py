#Sala de juegos EJERCICIO

edad=int(input("¿Cual es tu edad?:"))

if edad < 5:
    precio = 0
elif edad <= 18:
    precio = 5000
else:
    precio = 10000
    
if precio == 0:
    print("El cliente entra gratis.")
else:
    print(f"El precio de la entrada es: ${precio:,} pesos")
