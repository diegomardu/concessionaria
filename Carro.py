from Motor import Motor

class Carro:
    def __init__(self, nome="", ano=0, cor=""):
        self._nome = nome
        self._ano = ano
        self._cor = cor
        self._motor = None

    def getNome(self):
        return self._nome
    def setNome(self, nome):
        self._nome = nome

    def getAno(self):
        return self._ano
    def setAno(self, ano):
        self._ano = ano

    def getCor(self):
        return self._cor
    def setCor(self, cor):
        self._cor = cor

    def defineMotor(self,pot):
        self._motor = Motor(pot,cilindrada =0,combustivel = "Gasolina")

    def getMotor(self):
        return self._motor