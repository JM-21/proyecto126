from tkinter.messagebox import NO


class usuario():
    
    numUsusarios = 0

    def __init__(self, nombre, contra):
        self.nombre = nombre
        self.contra = contra

        self.conectado = False
        self.intentos = 5

        usuario.numUsusarios += 1

    def conectar(self, contrasenia=None):
        if contrasenia==None:
            myContra = input("Ingrese contraseña: ")
            while len(myContra) < 8:
                myContra = input("Ingrese contraseña valida: ")
        else:
            myContra=contrasenia
        if myContra==self.contra:
            print("Se ha conectado con exito")
            self.conectado = True
            return True
        else:
            self.intentos -= 1
            if self.intentos > 0:
                print("Contraseña incorrecta, intentelo de nuevo")
                if contrasenia!=None:
                     return False
                print("Intentos restantes", self.intentos)
                self.conectar()
            else:
                print("Error, no se pudo iniciar sesion")
                print("Hasta luego")
    def desconectar(self):
        if self.conectado:
            print("Se cerro sesion con exito")
            self.conectado = False
        else:
            print("Error, no has iniciado sesion")

    def __str__(self):
        if self.conectado:
            conect = "conectado"
        else:
            conect = "desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {conect}"

    