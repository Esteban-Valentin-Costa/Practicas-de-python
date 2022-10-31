from email.mime import application
from itertools import product
from ssl import CERT_NONE
from tkinter import ttk
from tkinter import *

import sqlite3
from unicodedata import name


"""  ESTA ES LA FORMA DE 
    HACER VAROS COMENTARIOS 
    A LA VEZ """

class Product:
    
    db_name = "database.db"
    
    def __init__(self,window):
        self.wind = window
        self.wind.title("Aplicacion de preducto")
        
        # Creating a Freme Container 
        frame = LabelFrame(self.wind, text = "Register a new Product")
        frame.grid(row = 0, column = 0, columnspan= 3, pady = 20)
        
        #Name Input
        Label(frame, text= "Name:").grid(row= 1 ,column= 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column = 1)
        
        # Price Input
        Label(frame, text= "Price").grid(row = 2, column= 0)
        self.price = Entry(frame)
        self.price.grid(row =2 , column = 1)
        
        # Save Products
        ttk.Button(frame, text= "Save Product",command= self.add_product).grid(row= 3, columnspan = 2, sticky= W + E )
        
        # Ouput Messages
        self.message = Label(text = "" , fg = "red")
        self.message.grid(row = 3, column= 0, columnspan= 2, sticky= W + E)
        
        #Tabel
        self.tree = ttk.Treeview(height= 10, column = 2)
        self.tree.grid(row= 4, column= 0, columnspan=2)
        self.tree.heading("#0",text="Name", anchor=CENTER)
        self.tree.heading("#1",text="Price",anchor=CENTER)
        
        # Deleting element 
        ttk.Button(text= "Delet",command= self.delete_product).grid(row=5 ,column = 0, sticky= W + E)
        
        #edit element
        ttk.Button(text= "Edit").grid(row=5 ,column = 1, sticky= W + E)
        

        self.get_products()
      
    def run_query(self,query,parameters = ()):
        with sqlite3.connect(self.db_name) as conn: 
            cursor = conn.cursor()
            result = cursor.execute(query,parameters)
            conn.commit()
        return result
    
    def get_products(self):
        #DELEITING ELEMENTS FROM THE TABLE
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # QUERING DATA 
        query = "SELECT * FROM Product ORDER BY name DESC" 
        db_rows = self.run_query(query)
        #FILLING DATE
        for row in db_rows:
            self.tree.insert("",0,text= row[1],values= row[2])
            
    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0
            
    def add_product (self):
        if self.validation():
            query = "INSERT INTO product VALUES(NULL, ?, ?)"
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters) 
            self.message["text"] = "Producasdft{}added Successfully" .format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message["text"] = "Name and product are required"

        self.get_products()
        
    def delete_product (self):
        try:
            self.tree.item(self.tree.selection())["text"]
        except IndexError as e:
            self.message["text"] = "Please select a record"
            return
        name = self.tree.item(self.tree.selection())["text"]
        query = "DELETE FROM product WHEAR name = ?"
        self.run_query(query,(name))
        

if __name__ == "__main__":
    window = Tk()
    application = Product(window)
    window.mainloop()
