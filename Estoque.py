#coding: utf-8

from Produtos import produto


class estoque:

    def __init__(self):
        self.listaProdutos = []
        self.total_caixa = 0.0

    def cadastroP(self):
        print("\n= = = = Cadastro de Produtos= = = =")
        while True:
            cont=0
            nome = raw_input("\nDigite o nome do produto: ")
            for i in range(len(self.listaProdutos)):
                if nome == self.listaProdutos[i].getNome():
                    cont+=1
            if cont==0:
                preco= float(raw_input("Digite o preço unitário do produto: "))
                while preco <=0:
                    preco=float(raw_input("Você não pode inserir um preço negativo ou igual a 0, digite novamente! "))
                tipo= raw_input("Digite o tipo do produto: ")
                estoque= int(raw_input("Digite a quantidade no estoque: "))
                while estoque <=0:
                    estoque= int(raw_input("Você não pode inserir um estoque negativo, digite novamente!"))
                prod = produto(nome,preco,tipo,estoque)
                self.listaProdutos.append(prod)
                print "\n%d %s(s) cadastrado(s) com sucesso.\n" % (estoque, nome.title())
            else:
                print "\n%s já está cadastrado.\n" % (nome.title())

            sair= raw_input("Deseja cadastrar outro produto? ")
            if sair.upper()=="NAO":
                break
            while sair.upper() not in ("NAO", "SIM"):
                print "\nValor inválido!"
                sair=raw_input("\nDigite 'nao' para sair e 'sim' para continuar: ")

    def vendendo(self):

        print("\n= = = = Venda de Produtos= = = =")
        existe= False
        while True:
            nome= raw_input("\nDigite o nome do Produto: ")
            for i in range(len(self.listaProdutos)):
                if self.listaProdutos[i].getNome()== nome:
                    existe= True
                    print "==> %s (%s). R$ %.2f" % (self.listaProdutos[i].getNome().title(), self.listaProdutos[i].getTipo().title(), self.listaProdutos[i].getPreco())
                    qtd_produto = int(raw_input("Digite a quantidade que deseja vender: "))
                    while qtd_produto <=0:
                        qtd_produto = int(raw_input("Você não pode inserir uma quantidade negativa ou igual a 0, digite novamente : "))
                    if qtd_produto <= self.listaProdutos[i].getEstoque():
                        self.listaProdutos[i].setEstoque(self.listaProdutos[i].getEstoque()-qtd_produto)
                        self.total_caixa += qtd_produto * self.listaProdutos[i].getPreco()
                        print "==> Total arrecadado: R$ %.2f"%(qtd_produto*self.listaProdutos[i].getPreco())
                        break
                    else:
                        print "Não é possível vender pois não há %s suficiente."%self.listaProdutos[i].getNome()
                if existe==False and i+1== len(self.listaProdutos):
                    print "%s nao cadastrado no sistema"%nome.title()
                    break

            sair = raw_input("\nDeseja vender outro produto? ")
            if sair.upper() == "NAO":
                break
            while sair.upper() not in ("NAO", "SIM"):
                print "\nValor inválido!"
                sair = raw_input("\nDigite 'nao' para sair e 'sim' para continuar: ")


    def imprimirBalanco(self):
        total_previsto=0.0
        print ("\n= = = = Impressão de Balanço = = = =\n")
        print "Produtos cadastrados:\n"
        for i in range(len(self.listaProdutos)):
            print "%d) %s(%s). R$ %.2f"%(i+1,self.listaProdutos[i].getNome().title(), self.listaProdutos[i].getTipo().title(),self.listaProdutos[i].getPreco())
            print("\tRestante: %d\n")%self.listaProdutos[i].getEstoque()
            total_previsto+= self.listaProdutos[i].getPreco() * self.listaProdutos[i].getEstoque()
        print "Total arrecardado em vendas: R$ %.2f"%self.total_caixa
        print "\nTotal que pode ser arrecardado: R$ %.2f"%total_previsto
