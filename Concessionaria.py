from Motor import Motor
from Carro import Carro
class Concessionaria:
    def __init__(self):
        self._carros = []

    def adicionarCarro(self):
        carro = Carro("",0,"")
        carro.setNome(input("Nome do carro:"))
        carro.setCor(input("Cor do carro:"))
        carro.setAno(input("Ano do carro:"))
        carro.defineMotor(float(input("Potencia do Motor:")))
        self._carros.append(carro)


    def buscaCarroAno(self,ano):
        for i in self._carros:
            if ano == i.getAno():
                print(i.getNome(),i.getAno(),i.getCor())
    def busCarroPotencia(self,potencia):
        for i in self._carros:
            if potencia in self._carros:
                print(i.getNome(),i.getAno(),i.getCor())
