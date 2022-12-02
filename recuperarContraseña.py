import tkinter as tk
from tkinter import messagebox
import recuperarContraseña2

class RecuperarConseña(tk.Tk):

    def __init__(self, ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.title("Antioquia es fiesta")
        self.anchoVentana = 800
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        self.resizable(width=False, height=False)
        self.iconbitmap("images/icon.ico")
        self.fondo = tk.PhotoImage(file="images/fondore.png")
        self.fondo1 = tk.Label(self, image=self.fondo).place(x=0, y=0, relwidth=1, relheight=1)

        # Label titulo
        self.registrese = tk.Label(self,
                                     text="Recuperar Contraseña",
                                     bg='white',
                                     fg='black',
                                     font=("Comc sans MS ", 25, "bold")
                                     )
        self.registrese.place(x=83, y=70)

        # variables definidas
        self.usuario = tk.StringVar()

        # Label usuario
        self.labelUsuario = tk.Label(self,
                                     text="Usuario: ",
                                     bg='white',
                                     fg='black',
                                     font=("Comc sans MS ", 13, "bold")
                                     )
        self.labelUsuario.place(x=100, y=170)
        # entradas usuario
        self.entradaUsuario = tk.Entry(self, highlightthickness=2,
                                textvariable=self.usuario,
                                relief="flat",
                                bg='#FFFFFF',
                                font=("Comc sans MS ", 12, "bold"))
        self.entradaUsuario.place(width=210)
        self.entradaUsuario.place(x=190, y=170)

        # Boton Volver
        self.botonVolver = tk.Button(self,
                                       text="Atras",
                                       command=self.volver,
                                       cursor="hand2",
                                       bg='white',
                                       width=16,
                                       height=2,
                                       foreground='black',
                                       relief="flat",
                                       font=("Comc sans MS ", 13, "bold"))
        self.botonVolver.place(x=126, y=300)

        # Boton Recuperar
        self.botonRecuperar = tk.Button(self,
                                       text="Recuperar",
                                       command=self.recuperar,
                                       cursor="hand2",
                                       bg='white',
                                       width=16,
                                       height=2,
                                       foreground='black',
                                       relief="flat",
                                       font=("Comc sans MS ", 13, "bold"))
        self.botonRecuperar.place(x=426, y=300)


    def volver(self):
        self.destroy()
        self.ventana_anterior.update()
        self.ventana_anterior.deiconify()

    def recuperar(self):
        
        if self.entradaUsuario.get() :
            self.datoUsuario = self.entradaUsuario.get()
            self.destroy()
            recuperarContraseña2.RecuperarConseña2(self.ventana_anterior,self.datoUsuario)
            
        else:
            messagebox.showinfo(message="Ingrese el usuario para recuperar la contraseña", title="Recuperar Contraseña")    
        










