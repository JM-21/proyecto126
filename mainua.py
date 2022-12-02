import traceback
import tkinter
from tkinter import *
from tkinter import messagebox
import registrece
from sesion import Sesion
import ventana1 
import recuperarContraseña


class MainUA(tkinter.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("Antioquia es fiesta")

        self.anchoVentana = 1000
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        
        self.resizable(width=False, height=False)
        self.iconbitmap("images/icon.ico")
        self.fondoImage = tkinter.PhotoImage(file="images/fondologin.png")
        self.labelImage = tkinter.Label(self,bg='#FFFFFF', image=self.fondoImage).place(x=0, y=0, relwidth=1, relheight=1)

        # Titulo principal:
        self.titulo = Frame(self, background='yellow')
        self.titulo.place(in_=self, anchor="c", relx=0.5, rely=0.15)
        self.textoTitulo = Label(self.titulo, text="Antioquia es fiesta", font=("Monotype Corsiva",30),
        fg='#FFFFFF', background='green')
        self.textoTitulo.grid(row=0, column=0, padx=10, pady=10)

        # variables para el login:
        self.usuario = tkinter.StringVar()
        self.password = tkinter.StringVar()

        # Label del dato Usuario:
        self.labelUsuario = tkinter.Label(self,text="Usuario: ",bg=None,font=("Comc sans MS",13,"bold"))
        self.labelUsuario.place(x=400,y=150)
        # Campo para ingresar el usuario:
        self.entryUsuario = tkinter.Entry(self,textvariable=self.usuario,relief="flat",bg='#FFFFFF',
                                         font=("Comc sans MS",12,"bold"))
        self.entryUsuario.place(x=400,y=180)

         # Label de la contraseña:
        self.labelContraseña = tkinter.Label(self,text="Contraseña: ",bg=None,font=("Comc sans MS",13,"bold"))
        self.labelContraseña.place(x=400,y=240)
        # Campo para ingresar la contraseña:
        self.entryContraseña = tkinter.Entry(self,textvariable=self.password,show="*",relief="flat",bg='#FFFFFF',
                                         font=("Comc sans MS",12,"bold"))
        self.entryContraseña.place(x=400,y=270)

        # Botón para salir:
        self.botonSalir = tkinter.Button(self,text="Cerrar",command=self.cerrar,cursor="hand2",
        width=10,height=1,bg=None,relief="flat",font=("Monotype Corsiva",12,"bold"))
        self.botonSalir.place(x=880,y=15)

        # Botón para ingresar:
        self.botonIngresar = tkinter.Button(self,text="Ingresar",command=self.ingresar,cursor="hand2",
        width=10,height=1,bg=None,relief="flat",font=("Comc sans MS",12,"bold"))
        self.botonIngresar.place(x=430,y=320)

        # Botón para registrarse:
        self.botonRegistrece = tkinter.Button(self,text="Registrese",command=self.registrece,cursor="hand2",
        width=10,height=1,bg=None,relief="flat",font=("Comc sans MS",12,"bold"))
        self.botonRegistrece.place(x=430,y=380)

        # Botón para recuperar contraseña:
        self.botonRecuperar = tkinter.Button(self,text="¿Olvido su contraseña?",command=self.recuperar,cursor="hand2",
        width=30,height=1,bg=None, fg="black",relief="flat",font=("Comc sans MS",10,"underline"))
        self.botonRecuperar.place(x=370,y=550)





        self.mainloop()

    def cerrar(self):
        self.destroy()

    def ingresar(self):

        if Sesion.intentosIngreso == 3:
            messagebox.showinfo(message="Ha excedido el número de\n"
                                        "intentos para ingresar.\n"
                                        "El sistema se detendra.", title="Usuario Pirata")
            Sesion.intentosIngreso = 0                            
            self.destroy()

        nombre = self.usuario.get()
        contraseña = self.password.get()

        if nombre and contraseña:

            try:
                with open("datos/usuarios/usuarios.txt", 'r') as f:  # Leyendo a todos los usuarios
                    filas = f.readlines()  # crea una lista de usuarios

                usuarios = []  # creamos una lista vacia de usuarios

                for fila in filas:
                    usuario = fila.split(";")
                    usuarios.append(usuario) # Llenamos la lista usuarios contodos los usuarios

                f.close()

                usuarioHallado = False

                for usuario in usuarios:
                    if nombre == usuario[2] and contraseña == usuario[3]:
                        Sesion.id = usuario[0]
                        Sesion.nombre = usuario[1]
                        Sesion.usuario = usuario[2]
                        usuarioHallado = True
                        break

                if usuarioHallado :
                        self.ir_Ventana1()
                        self.entryUsuario.delete(0, 'end')
                        self.entryContraseña.delete(0, 'end')
                else:
                    self.entryUsuario.delete(0, tkinter.END)
                    self.entryUsuario.insert(0, "Usuario incorrecto")
                    self.entryUsuario.config(bg="red")

                    self.entryContraseña.delete(0, tkinter.END)
                    self.entryContraseña.insert(0, "Contraseña incorrecta")
                    self.entryContraseña.config(bg="red", show="")

                    Sesion.intentosIngreso += 1

                    messagebox.showinfo(message="No existe este usuario " + nombre +".\n"
                                                "NO existe esta contraseña " + contraseña + ".\n"
                                                "Intente nuevamente.", title="Dados inválidos")

                    self.entryUsuario.delete(0, tkinter.END)
                    self.entryUsuario.insert(0, "")
                    self.entryUsuario.config(bg="white")

                    self.entryContraseña.delete(0, tkinter.END)
                    self.entryContraseña.insert(0, "")
                    self.entryContraseña.config(bg="white", show="*")

            except Exception as ex:
                print(traceback.format_exc())

        else:
            messagebox.showinfo(message="Debe ingresar un usuario.\n"
                                        "Debe ingresar una contraseña.\n"
                                        "Intente nuevamente.", title="Dados inválidos")
 

    def registrece(self):
        self.withdraw()
        registrece.Registrese(self)

    def ir_Ventana1(self):
        self.withdraw()
        ventana1.Ventana1(self)   

    def recuperar(self):
        self.withdraw()
        recuperarContraseña.RecuperarConseña(self)

MainUA()



