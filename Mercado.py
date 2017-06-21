#coding: utf-8
from Estoque import estoque

class mercado:

    def mercado(self):
        esto = estoque()
        while True:
            print("\n= = = = Bem-vindo(a) ao EconomizaTec= = = =\n")
            print("Digite a opção desejada\n")
            print("1. Cadastrar um Produto")
            print("2. Vender um Produto")
            print("3. Imprimir Balanço")
            print("4. Sair")
            opcao = raw_input("\nOpção: ")
            if opcao == "1":

                esto.cadastroP()
            elif opcao=="2":
                esto.vendendo()
            elif opcao=="3":
                esto.imprimirBalanco()
            elif opcao == "4":
                print "\nFim de caixa."
                return "sair"

mec = mercado()
mec.mercado()