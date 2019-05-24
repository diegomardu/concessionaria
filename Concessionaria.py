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
        carro = Carro("",0,"")
        for carro in self._carros:
            if ano == carro.getAno():
                print(carro.getNome(),carro.getAno(),carro.getCor())
            else:
                print("Carro ano %s não localizado:"%(ano))
    def busCarro(self,potencia):
        for i in self._carros:
            if i == potencia:
                return i