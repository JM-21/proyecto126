import tkinter as tk
from sesion import Sesion
import ventana2
import suroeste
class Ventana1(tk.Toplevel):

    def __init__(self,ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.construirse()

    def construirse(self):
        self.title("Antioquia es fiesta")
        self.anchoVentana = 1000
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        self.resizable(width=True, height=True)
        self.configure(bg='#ffffff')
        self.iconbitmap("images/icon.ico")
        self.fondo = tk.PhotoImage(file="images/pueblo.png")
        self.fondo1 = tk.Label(self,
                               bg='#ffffff',
                               image=self.fondo)
        self.fondo1.place(  x=0,
                            y=30,
                            relwidth=1,
                            relheight=1)

        self.cabecera = tk.Label(self,
                                     text="Usuario conectado: "+Sesion.usuario,
                                     bg='green',
                                     fg='black',
                                     font=("Monotype Corsiva", 12, "bold")
                                     )
        self.cabecera.place(x=650,y=5)

        # Botones
        self.botonVentana2 = tk.Button(self,
                                      text="Ventana 2",
                                      cursor="hand2",
                                      command=self.ir_Ventana2,
                                      bg='green',
                                      foreground='black',
                                      relief="flat",
                                      font=("Monotype Corsiva ", 10, "bold"))
        self.botonVentana2.place(x=100, y=60)

    

        self.botonVolver = tk.Button(self,
                                     text="Salir",
                                     cursor="hand2",
                                     command=self.salir,
                                     bg='green',
                                     foreground='black',
                                     relief="flat",
                                     font=("Monotype Corsiva ", 10, "bold"))
        self.botonVolver.place(width=80)
        self.botonVolver.place(x=900, y=5)

        self.botonDudas = tk.Button(self,
                                    text="?",
                                    cursor="hand2",
                                    width=3,
                                    height=1,
                                    bg='green',
                                    foreground='black',
                                    relief="flat",
                                    font=("Monotype Corsiva", 10, "bold"))
        self.botonDudas.place(x=50, y=60)

        self.Inicio = tk.Button(self,text="INICIO",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=0,y=100)
        self.Suroeste = tk.Button(self,text="Suroeste", command=self.ir_Suroeste,font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=80,y=100)
        self.Occidente = tk.Button(self,text="Occidente",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=158,y=100)
        self.Oriente = tk.Button(self,text="Oriente",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=248,y=100)
        self.Norte = tk.Button(self,text="Norte",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=320,y=100)
        self.Valle_de_Aburrá = tk.Button(self,text="Valle de aburrá",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=381,y=100)
        self.Bajo_Cauca = tk.Button(self,text="Bajo Cauca",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=508,y=100)
        self.Nordeste = tk.Button(self,text="Nordeste",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=607,y=100)
        self.Urabá = tk.Button(self,text="Urabá",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=690,y=100)
        self.Magdalena_Medio = tk.Button(self,text="Magdalena Medio",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=755,y=100)
        self.Filtrar = tk.Button(self,text="FILTRAR",font=("Monotype Corsiva",15),background="#00986C",fg="#EFFD5F").place(x=904,y=100)

    def salir(self):
        self.destroy()
        self.ventana_anterior.update()
        self.ventana_anterior.deiconify()

    def ir_Ventana2(self):        
        self.destroy()
        ventana2.Ventana2(self.ventana_anterior)

    def ir_Suroeste(self):
        self.destroy()
        suroeste.Suroeste(self.ventana_anterior)