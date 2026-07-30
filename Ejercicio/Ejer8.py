#Estructura FOR

frutas = ["apple", "banana", "cherry"]
for fruta in frutas:
  print(fruta)
  
frutas = ["apple", "banana", "cherry"]
for fruta in frutas:
  print(fruta)
  if fruta == "banana":
    break

for x in range(2,30,3):
  print(x)
  
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")