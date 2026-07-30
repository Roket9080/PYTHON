#Ejercicios Alumnos

nombre = input("¿Cual es tu nombre?:")
sexo = input("¿Cual es tu sexo (M para mujer y H para hombre)")

primera_letra = nombre[0].upper()

if(sexo == "M" and primera_letra < "M") or (sexo == "H" and primera_letra > "N"):
    grupo = "A"
else:
    grupo = "B"
    
print(f"Te corresponde el Grupo {grupo}")    