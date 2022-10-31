import tkinter as tk
ventana = tk.Tk()
ventana.title("prueba de tkinter")
ventana.geometry("600x400")

def Unir_mensaje():
    
    texto = f"hola me llamo {nombre1.get().strip()} y estoy en {Lugar.get().strip()} con {nombre2.get().strip()} y estamos haciendo {Accion.get().strip()}"
    Mensaje.config(text=texto)




### DANDO FORMA AL CAMVAS ###
tk.Label(ventana,text = "Primer nombre",
         fg="white",
         bg="black",
         width=20 ,
         height=1).pack()
nombre1 = tk.StringVar()
nomb1 = tk.Entry(ventana,textvariable=nombre1).pack()

tk.Label(ventana,
         text = "Segundo nombre",
         fg="white",
         bg="black",
         width=20 ,
         height=1
         ).pack()

nombre2 = tk.StringVar()
nomb2 = tk.Entry(ventana,textvariable=nombre2).pack()

tk.Label(ventana,text = "Lugar",
         fg="white",
         bg="black",
         width=20 ,
         height=1).pack()
Lugar = tk.StringVar()
lugar = tk.Entry(ventana,textvariable=Lugar).pack()

tk.Label(ventana,text = "accion en precente",
         fg="white",
         bg="black",
         width=20 ,
         height=1).pack()
Accion = tk.StringVar()
accion = tk.Entry(ventana,textvariable=Accion).pack()

Mensaje = tk.Label(ventana)
Mensaje.pack()

button = tk.Button(ventana,text="Mostrar mensaje loco", command=Unir_mensaje).pack()


ventana.mainloop() ## FIN DEL CAMVAS 



    


# # pedimos los datos 
# nombre1= input("nombre: ")
# ventana.mainloop()
# nombre2= input ("otro nombre: ")
# lugar= input("lugar: ")
# vervo= input("vervo: ")




# texto = f"hola me llamo {nombre1_l} y estoy en {lugar_l} con {nombre2_l} y estamos haciendo {vervo_l}"

# print (texto)


 