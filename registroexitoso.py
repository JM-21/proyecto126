import tkinter as tk

class RegistroExitoso(tk.Tk):

    def __init__(self, ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.title("Geriatic Advance")
        self.anchoVentana = 1000
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        self.resizable(width=True, height=True)
        # self.iconbitmap("GA.ico")
        self.fondo = tk.PhotoImage(file="images/fiestas.png")
        self.fondo1 = tk.Label(self, image=self.fondo).place(x=0, y=0, relwidth=1, relheight=1)

        # Label titulo
        self.registrese = tk.Label(self,
                                     text="El usuario se ha registrado exitosamente.",
                                     bg='#FFFFFF',
                                     font=("Comc sans MS ", 20, "bold")
                                     )
        self.registrese.place(x=83, y=70)

        # Boton Continuar
        self.botonContinuar = tk.Button(self,
                                       text="Continuar",
                                       command=self.continuar,
                                       cursor="hand2",
                                       bg='#000000',
                                       width=16,
                                       height=2,
                                       foreground='#FFFFFF',
                                       relief="flat",
                                       font=("Comc sans MS ", 13, "bold"))
        self.botonContinuar.place(x=126, y=508)

    def continuar(self):
        self.destroy()
        self.ventana_anterior.update()
        self.ventana_anterior.deiconify()