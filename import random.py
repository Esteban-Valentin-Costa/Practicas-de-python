import random
from string import whitespace

rango = int(input(f"introduce un rango"))

numero_ran = random.randint(0,rango)

predicion = rango + 2


while predicion  != numero_ran:
    
    predicion = int(input(f"ingresa un valor entre 0 y {rango}: "))
    
    if predicion < numero_ran:
        print("intenta de vuelta tu numero es menor")
    elif predicion > numero_ran:
        print ("tu numero es mayor")
        
print("as asertado")
