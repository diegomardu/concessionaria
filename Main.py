from  Concessionaria import Concessionaria
from Motor import Motor
carro = Concessionaria()
while True:
    print('''1 - Cadastrar veiculo:\n2 - Pesquisar Veiculo\n3 - Sair:''')
    try:
        n = int(input(("Selecione Opção:")))
        if n == 1:
            carro.adicionarCarro()
        elif n == 2:
            op = int(input(("Realizar busca por:\n1 - Ano\n2 - Potencia\n")))
            if op == 1:
                carro.buscaCarroAno(input("Informe Ano do Carro:"))
            elif op == 2:
                carro.busCarroPotencia(float(input("Informe Potencia do Carro:")))
        elif n == 3:
            break
        else:
            print("Valor fornecido invalido")

    except ValueError:
        print("Valor fornecido invalido")