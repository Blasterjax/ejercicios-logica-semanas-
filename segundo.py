num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))
num3 = int(input("Ingrese el tercer numero entero: "))

if (num1 > num2) and (num1 > num3):
  mayor = num1
  if num2 > num3:
    mediano = num2
    menor = num3
  else:
    mediano = num3
    menor = num2

elif (num2 > num1) and (num2 > num3):
  mayor = num2
  if num1 > num3:
    mediano = num1
    menor = num3
  else:
    mediano = num3
    menor = num1

else:
  mayor = num3
  if num1 > num2:
    mediano = num1
    menor = num2
  else:
    mediano = num2
    menor = num1

print("El mayor es el ", mayor)
print("El mediano es el ", mediano)
print("El menor es el ", menor)
