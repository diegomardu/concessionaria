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
        self._carros.append(carro)

    def buscaCarro(self,ano):
        for i in self._carros:
            if ano == i.getAno():
                print(i.getNome(),i.getAno(),i.getCor())
    def busCarro(self,potencia):
        for i in self._carros:
            if potencia == i.getPotencia():
                print(i.getNome(),i.getAno(),i.getCor())
