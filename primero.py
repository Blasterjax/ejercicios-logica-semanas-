numero = int(input("Ingresa un número del 0 al 6: "))

if numero == 0:
  nombre_dia = "lunes"

elif numero == 1:
  nombre_dia = "martes"

elif numero == 2:
  nombre_dia = "miércoles"

elif numero == 3:
  nombre_dia = "jueves"

elif numero == 4:
  nombre_dia = "viernes"

elif numero == 5:
  nombre_dia = "sábado"

elif numero == 6:
  nombre_dia = "domingo"

if 0 <= numero <= 6:
  print("El día correspondiente al numero", numero, "es", nombre_dia)
else:
  print("Error: Ingrese un número del 0 al 6.")
