class Vehiculo:
    def __init__(self, nombre, asientos, motor, ruedas):
        self.name = nombre
        self.ruedas = ruedas
        self.asientos = asientos
        self.__motor = motor
        self.arrancado = False

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getMotor(self):
        return self.__motor

    def setMotor(self, motor):
        self.__motor = motor

    def dime_motor(self):
        return self.__motor

    def arranca_vehiculo(self):
        print("Arrancando vehiculo")
        self.arrancado = True

    def apaga_vehiculo(self):
        print("Apagando")
        self.arrancado = False

    def esta_arrancado(self):
        return "Si" if self.arrancado else "No"

    def __exclusivo_vehiculo(self):
        print("solo yo")

    def que_es(self):
        print("Es un vehiculo")


class Coche(Vehiculo):
    def __init__(self, nombre: str, asientos: int, motor: str):
        super().__init__(nombre, asientos, motor, 4)
        print("Has creado un coche")

    def __str__(self):
        return "El coche es un %s" % self.name


class Moto(Vehiculo):
    def __init__(self, nombre, asientos, motor):
        super().__init__(nombre, asientos, motor, 2)
        print("Has creado una moto")
        self.que_es()

    def haz_caballito(self):
        print("Haciendo caballito")

    def __str__(self):
        return "La moto es %s" % self.name

    def que_es(self):
        #super().que_es()
        print("Una moto")
