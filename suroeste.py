import tkinter as tk
from sesion import Sesion
import ventana1
import amaga
import jardin

class Suroeste(tk.Toplevel):

    def __init__(self,ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.construirse()

    def construirse(self):
        self.title("SurOeste")
        self.anchoVentana = 1000
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        self.resizable(width=True, height=True)
        self.configure(bg='#ffffff')
        self.iconbitmap("images/icon.ico")
        self.fondo = tk.PhotoImage(file="images/suroeste.png")
        self.fondo1 = tk.Label(self,
                               bg='gray',
                               image=self.fondo)
        self.fondo1.place(  x=0,
                            y=30,
                            relwidth=1,
                            relheight=1)

        self.cabecera = tk.Label(self,
                                     text="Usuario conectado: "+Sesion.usuario,
                                     bg='green',
                                     fg='black',
                                     font=("Monotype Corsiva ", 10, "bold")
                                     )
        self.cabecera.place(x=650,y=5)

        lbl_titulo = tk.Label(self,
                                 text=" Bienvenido al SurOeste Antioqueño \n Selecciona el pueblo de tu interes", fg="yellow", 
                                 bg="green", font=("Monotype Corsiva", 20))
        lbl_titulo.pack
        lbl_titulo.place(x= 300, y=100)

        # Botones
        self.botonVolver = tk.Button(self,
                                      text="Volver",
                                      cursor="hand2",
                                      command=self.volver,
                                      bg='green',
                                      foreground='#000000',
                                      relief="flat",
                                      font=("Monotype Corsiva", 15, "bold"))
        self.botonVolver.place(x=100, y=50)

        #Botones de los pueblos
        self.Amaga = tk.Button(self,text="Amaga", command=self.ir_amaga,font=("Monotype Corsiva",25),background="#00986C",fg="#EFFD5F").place(x=150,y=200)
        self.Amaga = tk.Button(self,text="Jardin", command=self.ir_jardin,font=("Monotype Corsiva",25),background="#00986C",fg="#EFFD5F").place(x=300,y=200)

        self.botonDudas = tk.Button(self,
                                    text="?",
                                    cursor="hand2",
                                    width=3,
                                    height=1,
                                    bg='green',
                                    foreground='#000000',
                                    relief="flat",
                                    font=("Monotype Corsiva ", 10, "bold"))
        self.botonDudas.place(x=50, y=70)


    def ir_amaga(self):
        self.destroy()
        amaga.Amaga(self.ventana_anterior)

    def ir_jardin(self):
        self.destroy()
        jardin.Jardin(self.ventana_anterior)

    def volver(self):
        self.destroy()
        ventana1.Ventana1(self.ventana_anterior)