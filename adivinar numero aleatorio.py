import random 

rango = int(input("pon un numero: "))
        
numero_ran = random.randint(1, rango)

prediccion = 0

while prediccion != numero_ran:

    prediccion = int(input(f"adivina un numero entre {rango}: "))
    
    if prediccion < numero_ran:
        print("tu numero es muy chico intentalo nuevamente")
    elif prediccion > numero_ran: 
        print("tu numero es muy grande")

print("as asertado")
    




