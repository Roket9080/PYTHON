#Ejercicio Salario 

salario=float(input("Ingrese su salario mensual: "))

if salario < 12000000:
    impuesto = 0
elif salario <= 15000000:
    impuesto = salario * 0.03
elif salario <= 20000000:
    impuesto = salario * 0.05
elif salario <= 30000000:
    impuesto = salario * 0.08
else:
    impuesto = salario * 0.10
    
print(f"El impuesto que debe pagar es: ${impuesto:,.2f}")