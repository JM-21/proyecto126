import tkinter as tk
from tkinter import messagebox
import recuperarContraseña

class RecuperarConseña2(tk.Tk):

    def __init__(self, ventana_anterior, usuario):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.usuario = usuario
        self.title("Fiestas Regionales de Colombia")
        self.anchoVentana = 1000
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        self.resizable(width=True, height=True)
        self.iconbitmap("images/icon.ico")
        self.fondo = tk.PhotoImage(file="images/fondore.png")
        self.fondo1 = tk.Label(self, image=self.fondo).place(x=0, y=0, relwidth=1, relheight=1)

        # Label titulo
        self.registrese = tk.Label(self,
                                     text="Recuperar Contraseña",
                                     bg='#000000',
                                     fg='#FFFFFF',
                                     font=("Comc sans MS ", 40, "bold")
                                     )
        self.registrese.place(x=83, y=40)

        try:
            with open("datos/usuarios/usuarios.txt", 'r') as f: # Leyendo a todos los usuarios
                filas = f.readlines()  # crea una lista de usuarios

            usuarios = []  #creamos una lista vacia de usuarios

            for fila in filas: # llenamos la lista con todos los usuarios de los registros del archivo
                usuario = fila.split(";") # Tomamos registro por registro y lo separamos por el ';'
                usuarios.append(usuario) # Lo agregamos como una lista

            f.close() # Cerramos el archivo

            

            #Variable para controlar si existe el usuario:
            existeUsuario = False
            usuarioExistente = []
            pregunta1 = ""
            pregunta2 = ""
            pregunta3 = ""
            # Recorremos todos los usuarios para buscar y comparar los datos de recuperación
            for usuario in usuarios:
                if (
                    self.usuario == usuario[2]                   
                ):
                    
                    existeUsuario = True # Existe el usuario
                    usuarioExistente = usuario 
                    break

            #Si los datos ingresados son correctos se recupera la contraseña
            if existeUsuario:

                pregunta1 = usuarioExistente[4]
                pregunta2 = usuarioExistente[6]
                pregunta3 = usuarioExistente[8]

            else:
                messagebox.showinfo(message="El usuario: "+self.usuario+" no existe en el sistema.", title="Dados inválidos")
                self.volver()
        except Exception as ex:
            print(ex)

        # Preguntas de validación para recuperar contraseña
        # variables definidas
        self.preguntaValidacion1 = tk.StringVar()
        self.preguntaValidacion2 = tk.StringVar()
        self.preguntaValidacion3 = tk.StringVar()

        # Label pregunta 1
        self.labelPregunta1 = tk.Label(self,
                                    text=pregunta1,
                                    bg='#FFFFFF',
                                    font=("Comc sans MS ", 13, "bold")
                                    )
        self.labelPregunta1.place(x=83, y=140)
        # entradas pregunta 1
        self.entradaPregunta1 = tk.Entry(self,
                                      textvariable=self.preguntaValidacion1,
                                      relief="flat",
                                      bg='#FFFFFF',
                                      font=("Comc sans MS ", 12, "bold"))
        self.entradaPregunta1.place(width=310)
        self.entradaPregunta1.place(x=83, y=164)

        # Label pregunta 2
        self.labelPregunta2 = tk.Label(self,
                                       text=pregunta2,
                                       bg='#FFFFFF',
                                       font=("Comc sans MS ", 13, "bold")
                                       )
        self.labelPregunta2.place(x=83, y=236)
        # entradas pregunta 2
        self.entradaPregunta2 = tk.Entry(self,
                                         textvariable=self.preguntaValidacion2,
                                         relief="flat",
                                         bg='#FFFFFF',
                                         font=("Comc sans MS ", 12, "bold"))
        self.entradaPregunta2.place(width=310)
        self.entradaPregunta2.place(x=83, y=260)

        # Label pregunta 3
        self.labelPregunta3 = tk.Label(self,
                                       text=pregunta3,
                                       bg='#FFFFFF',
                                       font=("Comc sans MS ", 13, "bold")
                                       )
        self.labelPregunta3.place(x=83, y=330)
        # entradas pregunta 3
        self.entradaPregunta3 = tk.Entry(self,
                                         textvariable=self.preguntaValidacion3,
                                         relief="flat",
                                         bg='#FFFFFF',
                                         font=("Comc sans MS ", 12, "bold"))
        self.entradaPregunta3.place(width=310)
        self.entradaPregunta3.place(x=83, y=354)

        # Boton Volver
        self.botonVolver = tk.Button(self,
                                       text="Volver",
                                       command=self.volver,
                                       cursor="hand2",
                                       bg='#000000',
                                       width=16,
                                       height=2,
                                       foreground='#FFFFFF',
                                       relief="flat",
                                       font=("Comc sans MS ", 13, "bold"))
        self.botonVolver.place(x=126, y=455)

        # Boton Recuperar
        self.botonRecuperar = tk.Button(self,
                                       text="Recuperar",
                                       command=self.recuperar,
                                       cursor="hand2",
                                       bg='#000000',
                                       width=16,
                                       height=2,
                                       foreground='#FFFFFF',
                                       relief="flat",
                                       font=("Comc sans MS ", 13, "bold"))
        self.botonRecuperar.place(x=426, y=455)


    def volver(self):
        self.destroy()
        recuperarContraseña.RecuperarConseña(self.ventana_anterior)

    def recuperar(self):

        

        if not self.entradaPregunta1.get() or self.entradaPregunta1.get() == "Ingresa la respuesta 1":
            self.entradaPregunta1.delete(0, tk.END)
            self.entradaPregunta1.insert(0, "Ingresa la respuesta 1")
            self.entradaPregunta1.config(bg="gray")

        if not self.entradaPregunta2.get() or self.entradaPregunta2.get() == "Ingresa la respuesta 2":
            self.entradaPregunta2.delete(0, tk.END)
            self.entradaPregunta2.insert(0, "Ingresa la respuesta 2")
            self.entradaPregunta2.config(bg="gray")

        if not self.entradaPregunta3.get() or self.entradaPregunta3.get() == "Ingresa la respuesta 3":
            self.entradaPregunta3.delete(0, tk.END)
            self.entradaPregunta3.insert(0, "Ingresa la respuesta 3")
            self.entradaPregunta3.config(bg="gray")

        if (
            (self.entradaPregunta1.get() and self.entradaPregunta1.get() != "Ingresa la respuesta 1") and
            (self.entradaPregunta2.get() and self.entradaPregunta2.get() != "Ingresa la respuesta 2") and
            (self.entradaPregunta3.get() and self.entradaPregunta3.get() != "Ingresa la respuesta 3")
          ):

            try:
                with open("datos/usuarios/usuarios.txt", 'r') as f: # Leyendo a todos los usuarios
                    filas = f.readlines()  # crea una lista de usuarios

                usuarios = []  #creamos una lista vacia de usuarios

                for fila in filas: # llenamos la lista con todos los usuarios de los registros del archivo
                    usuario = fila.split(";") # Tomamos registro por registro y lo separamos por el ';'
                    usuarios.append(usuario) # Lo agregamos como una lista

                f.close() # Cerramos el archivo

                #Variable para recuperar la contraseña
                contraseña = ""

                #Variable para controlar si se recupero la contraseña
                recuperada = False

                # Recorremos todos los usuarios para buscar y comparar los datos de recuperación
                for usuario in usuarios:
                    if (
                        self.usuario == usuario[2] and
                        self.entradaPregunta1.get() == usuario[5] and
                        self.entradaPregunta2.get() == usuario[7] and
                        self.entradaPregunta3.get() == usuario[9]
                    ):
                        contraseña = usuario[3] # si los datos son correctos
                        recuperada = True

                #Si los datos ingresados son correctos se recupera la contraseña
                if recuperada:

                    messagebox.showinfo(message="Su contraseña es: "+contraseña+"\nNo la vuelvas a olvidar.", title="Contraseña Recuperada")
                    self.volver()


                else:
                    messagebox.showinfo(message="Los datos ingresados son incorrectos \nIntente nuevamente.\n"
                                                "Verifique que el usuario sea el correcto.\n"
                                                "Verifique que las respuestas sean correctas.", title="Dados inválidos")
            except Exception as ex:
                print(ex)











