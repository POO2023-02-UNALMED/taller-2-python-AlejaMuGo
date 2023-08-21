class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(self,color):
        if color in ["rojo","verde","amarillo","negro","blanco"]:
            self.color = color
class Motor:
    def __init__(self, numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self,registro):
        self.registro = registro
    def asignarTipo(self,tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

class Auto:
    cantidadCreados = int
    def __init__(self, modelo, precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.marca=marca
        self.registro=registro
        self.motor = motor
        self.asientos = list(asientos)
    def cantidadAsientos(self):
        contador = 0
        for i in range(len(self.asientos)):
            if type(self.asientos[i]) == Asiento:
                contador +=1
        return contador
    def verificarIntegridad(self):
        iguales = True
        for i in range(len(self.asientos)):
            if (type(self.asientos[i]) == Asiento):
                if (self.asientos[i].registro != self.registro):
                    iguales = False
        if (iguales == True and self.registro == self.motor.registro):
            return "Auto original"
        else:
            return "Las piezas no son originales"






