import traceback
import tkinter as tk
from tkinter import messagebox
from registroexitoso import RegistroExitoso

class Registrese(tk.Toplevel):

    def __init__(self, ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.title("Registrese")
        self.anchoVentana = 1000
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        self.resizable(width=True, height=True)
        self.iconbitmap("images/icon.ico")
        # self.configure(background="#008B45")
        self.fondo = tk.PhotoImage(file="images/pueblo.png")
        self.fondo1 = tk.Label(self, image=self.fondo).place(x=0, y=0, relwidth=1, relheight=1)

        # Label titulo
        self.registrese = tk.Label(self,
                                     text="Regístrese",
                                     bg="#F0F0F0",
                                     font=("Comc sans MS ", 40, "bold")
                                     )
        self.registrese.place(x=83, y=70)

        # variables definidas
        self.nombreCompleto = tk.StringVar()
        self.usuario = tk.StringVar()
        self.password = tk.StringVar()


        # Label nombre completo
        self.labelNombre = tk.Label(self,
                                     text="Nombre Completo:",
                                     bg="#F0F0F0",
                                     font=("Comc sans MS ", 13, "bold")
                                     )
        self.labelNombre.place(x=83, y=192)
        # entradas nombre completo
        self.entradaNombre = tk.Entry(self, highlightthickness=2,
                                       textvariable=self.nombreCompleto,
                                       relief="flat",
                                       bg="#FFFFFF",
                                       font=("Comc sans MS ", 12, "bold"))
        self.entradaNombre.place(width=300)
        self.entradaNombre.place(x=83, y=224)

        # Label usuario
        self.labelUsuario = tk.Label(self,
                                     text="Usuario:",
                                     bg="#F0F0F0",
                                     font=("Comc sans MS ", 13, "bold")
                                     )
        self.labelUsuario.place(x=83, y=289)
        # entradas usuario
        self.entradaUsuario = tk.Entry(self,highlightthickness=2,
                                textvariable=self.usuario,
                                relief="flat",
                                bg="#FFFFFF",
                                font=("Comc sans MS ", 12, "bold"))
        self.entradaUsuario.place(x=83, y=321)

        # Label contraseña
        self.labelContraseña = tk.Label(self,
                                        text="Contraseña:",
                                        bg="#F0F0F0",
                                        font=("Comc sans MS ", 13, "bold")
                                        )
        self.labelContraseña.place(x=83, y=386)
        # entrada contraseña
        self.entradaContraseña = tk.Entry(self, highlightthickness=2,
                                          textvariable=self.password,
                                          show="•",
                                          relief="flat",
                                          bg="#FFFFFF",
                                          font=("Comc sans MS ", 12, "bold"))
        self.entradaContraseña.place(width=300)
        self.entradaContraseña.place(x=83, y=418)

        # Boton Cancelar
        self.botonIngresar = tk.Button(self,
                                       text="Cancelar",
                                       command=self.cancelar,
                                       cursor="hand2",
                                       bg="#000000",
                                       foreground="#FFFFFF",
                                       relief="flat",
                                       font=("Comc sans MS ", 13, "bold"))
        self.botonIngresar.place(x=126, y=508)

        # Preguntas de validación para recuperar contraseña
        # variables definidas
        self.preguntaValidacion1 = tk.StringVar()
        self.respuestaValidacion1 = tk.StringVar()
       

        # Label pregunta 1
        self.labelPregunta1 = tk.Label(self,
                                    text="Escribe la pregunta 1 para recuperar la contraseña:",
                                    bg="#F0F0F0",
                                    font=("Comc sans MS ", 13, "bold")
                                    )
        self.labelPregunta1.place(x=450, y=50)
        # entradas pregunta 1
        self.entradaPregunta1 = tk.Entry(self, highlightthickness=2,
                                      textvariable=self.preguntaValidacion1,
                                      relief="flat",
                                      bg="#F5F5F5",
                                      font=("Comc sans MS ", 12, "bold"))
        self.entradaPregunta1.place(width=400)                              
        self.entradaPregunta1.place(x=450, y=82)
         # Label pregunta 1
        self.labelRepuestaPregunta1 = tk.Label(self,
                                    text="Escribe la respuesta de la pregunta 1 para recuperar la contraseña:",
                                    bg="#F0F0F0",
                                    font=("Comc sans MS ", 13, "bold")
                                    )
        self.labelRepuestaPregunta1.place(x=450, y=130)
        # entradas pregunta 1
        self.entradaRepuestaPregunta1 = tk.Entry(self, highlightthickness=2,
                                      textvariable=self.respuestaValidacion1,
                                      relief="flat",
                                      bg="#F5F5F5",
                                      font=("Comc sans MS ", 12, "bold"))
        self.entradaRepuestaPregunta1.place(width=400)                              
        self.entradaRepuestaPregunta1.place(x=450, y=162)


        # Pregunta de recuperar contraseña 2:

       
        # entradas pregunta 1
        


       
        
        

        # Boton Regístrese
        self.botonRegistrese = tk.Button(self,
                                       text="Regístrese",
                                       command=self.registrece,
                                       cursor="hand2",
                                       bg="#000000",
                                       foreground="#FFFFFF",
                                       relief="flat",
                                       font=("Comc sans MS ", 13, "bold"))
        self.botonRegistrese.place(x=626, y=508)


    def cancelar(self):
        self.destroy()
        self.ventana_anterior.update()
        self.ventana_anterior.deiconify()

    def registrece(self):

        if not self.entradaNombre.get() or self.entradaNombre.get() == "Ingrese el Nombre":
            self.entradaNombre.delete(0, tk.END)
            self.entradaNombre.insert(0, "Ingrese el Nombre")
            self.entradaNombre.config(bg="gray")

        if not self.entradaUsuario.get() or self.entradaUsuario.get() == "Ingrese el Usuario":
            self.entradaUsuario.delete(0, tk.END)
            self.entradaUsuario.insert(0, "Ingrese el Usuario")
            self.entradaUsuario.config(bg="gray")

        if not self.entradaContraseña.get() or self.entradaContraseña.get() == "Ingrese la contraseña":
            self.entradaContraseña.delete(0, tk.END)
            self.entradaContraseña.insert(0, "Ingrese la contraseña")
            self.entradaContraseña.config(bg="gray", show="")

        if len(self.entradaContraseña.get()) < 8:
            self.entradaContraseña.delete(0, tk.END)
            self.entradaContraseña.insert(0, "Debe ser de minimo 8 caracteres")
            self.entradaContraseña.config(bg="gray", show="")

        if (self.entradaContraseña.get() != "Ingrese la contraseña" and
        not any(char.isdigit() for char in self.entradaContraseña.get())
        ):
            self.entradaContraseña.delete(0, tk.END)
            self.entradaContraseña.insert(0, "Debe tener números")
            self.entradaContraseña.config(bg="gray", show="")    

        if (self.entradaContraseña.get() != "Ingrese la contraseña" and
        not any(char.isalpha() for char in self.entradaContraseña.get())
        ):
            self.entradaContraseña.delete(0, tk.END)
            self.entradaContraseña.insert(0, "Debe tener letras")
            self.entradaContraseña.config(bg="gray", show="") 

        if (self.entradaContraseña.get() != "Ingrese la contraseña" and
           self.entradaContraseña.get().isalnum()
        ):
            self.entradaContraseña.delete(0, tk.END)
            self.entradaContraseña.insert(0, "Debe tener caracteres especiales")
            self.entradaContraseña.config(bg="gray", show="")   

        if (self.entradaContraseña.get() != "Ingrese la contraseña" and
        not any(char.isupper() for char in self.entradaContraseña.get())
        ):
            self.entradaContraseña.delete(0, tk.END)
            self.entradaContraseña.insert(0, "Debe tener letras en mayusculas")
            self.entradaContraseña.config(bg="gray", show="")           

        if not self.entradaPregunta1.get() or self.entradaPregunta1.get() == "Escribe la pregunta 1":
            self.entradaPregunta1.delete(0, tk.END)
            self.entradaPregunta1.insert(0, "Escribe la pregunta 1")
            self.entradaPregunta1.config(bg="gray")

       

        if not self.entradaRepuestaPregunta1.get() or self.entradaRepuestaPregunta1.get() == "Escribe la respuesta 1":
            self.entradaRepuestaPregunta1.delete(0, tk.END)
            self.entradaRepuestaPregunta1.insert(0, "Escribe la respuesta 1")
            self.entradaRepuestaPregunta1.config(bg="gray")        

        if (
            (self.entradaNombre.get() and self.entradaNombre.get() != "Ingrese el Nombre")and
            (self.entradaUsuario.get() and self.entradaUsuario.get() != "Ingrese el Usuario")and
            (self.entradaContraseña.get() and
             self.entradaContraseña.get() != "Ingrese la contraseña" and
             self.entradaContraseña.get() != "Debe ser de minimo 8 caracteres" and 
             self.entradaContraseña.get() != "Debe tener letras" and
             self.entradaContraseña.get() != "Debe tener números" and
             self.entradaContraseña.get() != "Debe tener caracteres especiales" and
             self.entradaContraseña.get() != "Debe tener letras en mayusculas"
            )and
            (self.entradaPregunta1.get() and self.entradaPregunta1.get() != "Escribe la pregunta 1")and

            (self.entradaRepuestaPregunta1.get() and self.entradaRepuestaPregunta1.get() != "Escribe la respuesta 1")
            ) :

            try:
                with open("datos/usuarios/usuarios.txt", 'r') as f: # Leyendo a todos los usuarios
                    filas = f.readlines()  # crea una lista de usuarios

                usuarios = []  #creamos una lista vacia de usuarios

                usuarioLogins = []

                contraseñasLogins = []

                for fila in filas:
                    usuario = fila.split(";")
                    usuarios.append(usuario)
                f.close()

                for usuario in usuarios:
                    usuarioLogins.append(usuario[2])
                    contraseñasLogins.append(usuario[3])

                if ( self.entradaUsuario.get() not in usuarioLogins and
                    self.entradaContraseña not in contraseñasLogins ):

                    f = open("datos/usuarios/clave.txt", "r")  # Consultando la clave actual
                    clave_actual = f.read()
                    f.close()

                    clave_nueva = int(clave_actual) + 1 # Aumentando en 1 la clave

                    f = open("datos/usuarios/clave.txt", "w")
                    f.write(str(clave_nueva))    # Actualizando la nueva clave
                    f.close()

                    f = open("datos/usuarios/usuarios.txt", "a")
                    f.write(
                        str(clave_nueva)+";"+              #0
                        self.entradaNombre.get()+";"+      #1
                        self.entradaUsuario.get()+";"+     #2
                        self.entradaContraseña.get()+";"+  #3
                        self.entradaPregunta1.get()+";"+  #4
                        self.entradaRepuestaPregunta1.get()+";" #5
                    )
                    f.close()
                    self.destroy()
                    RegistroExitoso(self.ventana_anterior)
                else:
                    messagebox.showinfo(message="Intente con otro usuario \ny con otra contreseña.\n"
                                                "Ya existe este usuario.\n"
                                                "Ya existe esta contraseña", title="Dados inválidos")

            except Exception as ex:
                print(traceback.format_exc())


