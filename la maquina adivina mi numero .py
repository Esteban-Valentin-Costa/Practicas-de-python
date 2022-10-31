import random


print("Voy a tratar de adivinar tu numero")
rango = int(input("pon un numero: ")) 
print(f"elige un numero del 1 al {rango} y anotalo ")

######### FUNCION PARA GENEREAR NUMEROS RANDO DESDE UN VALOR A OTRO ########
def numero_ram (a,b):
    numero = random.randint(a,b)
    return numero


adivinar = numero_ram(1,rango)
print (f"tu numero es este: {adivinar}, pon si o no ")
correcto = input(": ")

min= 1 
max = rango

while correcto == "no":
    
    print(f"¿{adivinar} es mas grande que tu numero?")
    Mayor = input(": ")
    
    if Mayor == "si":
        max = adivinar   
        
    elif Mayor == "no":
        min = adivinar
    
    adivinar = numero_ram(min,max)
    print (f"tu numero es este {adivinar}")
    correcto = input(": ")
        
        
   

     
            
    
    




