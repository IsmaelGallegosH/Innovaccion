# program.py
sum = 1 + 2
product = sum * 2
print(product)

# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())
print("Today's date is: " + str(date.today()))

#introduccir datos
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")

#concatenacion
print(first_number + second_number)

#Suma
print(int(first_number) + int(second_number))