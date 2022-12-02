from tkinter import *
import tkinter as tk
def fsur():
    print("soy sur")
ventana = Frame(height=670,width=1000)
ventana.pack(padx=20,pady=20)

#Imagen de fondo
imagen = PhotoImage(file="images/fondoboton.png")
Label(ventana, image=imagen, bd = 0).pack()

#Botones
Inicio = Button(ventana,text="INICIO",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=10,y=100)
Suroeste = Button(ventana,text="Suroeste",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=90,y=100)
Occidente = Button(ventana,text="Occidente",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=168,y=100)
Oriente = Button(ventana,text="Oriente",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=258,y=100)
Norte = Button(ventana,text="Norte",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=330,y=100)
Valle_de_Aburrá = Button(ventana,text="Valle de aburrá",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=391,y=100)
Bajo_Cauca = Button(ventana,text="Bajo Cauca",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=518,y=100)
Nordeste = Button(ventana,text="Nordeste",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=617,y=100)
Urabá = Button(ventana,text="Urabá",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=700,y=100)
Magdalena_Medio = Button(ventana,text="Magdalena Medio",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=765,y=100)
Filtrar = Button(ventana,text="FILTRAR",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=914,y=100)


ventana.mainloop()