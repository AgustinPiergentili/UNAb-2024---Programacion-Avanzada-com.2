import cuentaBancaria_bd


class CuentaBancaria():
    ''' Clase que nos permite la gestión de una Cuenta Bancaria genérica!
    '''
    
    def __init__(self, saldo_inicial, nombre, apellido, moneda = '$'):
        # TODO: Ver la forma de soportar cajas de ahorro y/o cuentas corrientes
        self.movimientos = []
        self.saldo = saldo_inicial
        self.nombre = nombre
        self.apellido = apellido
        self.moneda = moneda

    def depositar(self, monto):
        '''Método que nos permite realizar un depósito bancario'''
        self.movimientos.append('DEPOSITO: ' + str(monto))
        self.saldo = self.saldo + monto


    def extraer(self, monto):
        '''Método que nos permite realizar una extracción de un cuenta bancaria'''
        if self.saldo - monto >= 0:
            self.movimientos.append('EXTRACCION: ' + str(monto))
            self.saldo = self.saldo - monto
        else:
            self.movimientos.append('SALDO INSUFICIENTE: ' + str(monto)) 
            print("Saldo insuficiente")
        

    def datos_titular(self):
        '''Método que nos permite mostrar los datos del titular y su saldo'''
        return self.apellido + ', ' + self.nombre + " con el saldo: " + str(self.saldo) + " " + self.moneda
    
    def datos_saldo(self):
        return self.saldo

    def _reset_saldo(self):
        self.saldo = 0 

    def datos_movimientos(self):
        return list(self.movimientos)  



class User:

    def __init__(self, nombre, contrasena, apellido, dni):
        self.nombre = nombre
        self.contrasena = contrasena
        self.apellido = apellido
        self.dni = dni

    @staticmethod
    def registrar_usuario():
        nombre = input("Ingrese un nombre de usuario: ")
        contrasena = input("Ingrese una contraseña: ")
        apellido = input("Ingrese su apellido: ")
        dni = input("Ingrese DNI: ")
        nuevo_usuario = User(nombre, contrasena, apellido, dni)
        print("Usuario registrado correctamente.")
        return nuevo_usuario

    def iniciar_sesion(self,nombre,contrasena):
        if self.nombre == nombre and self.contrasena == contrasena:
            self.conectado = True
            print("Inicio de sesión exitoso.")
        else:
            print("Nombre de usuario o contraseña incorrectos.")

    def cerrar_sesion(self):
        self.conectado = False
        print("Sesión cerrada.")

    def esta_conectado(self):
        return self.conectado
    


