from Motor import Motor
from Carro import Carro
class Concessionaria:
    def __init__(self):
        self._carros = []

    def adicionarCarro(self):
        carro = Carro("",0,"")
        carro = Motor(0,0,"")
        carro.setNome(input("Nome do carro:"))
        carro.setCor(input("Cor do carro:"))
        carro.setAno(input("Ano do carro:"))
        carro.setPotencia(input("Potencia do Carro:"))
        carro.setCilindrada(input("Cilindrada do Carro:"))
        self._carros.append(carro)

    def buscaCarro(self,ano):
        for i in self._carros:
            if ano == i.getAno():
                print(i.getNome(),i.getAno(),i.getCor())
            else:
                print("Carro ano %s não localizado:"%(ano))
    #def busCarro(self,potencia):
