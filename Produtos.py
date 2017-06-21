#coding: utf-8

class produto:
    def __init__(self, nome, preco, tipo,estoque):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
        self.estoque = estoque

    def getNome(self):
        return self.nome

    def getPreco(self):
        return self.preco

    def getTipo(self):
        return self.tipo

    def getEstoque(self):
        return self.estoque

    def setEstoque(self, outroEstoque):
        self.estoque = outroEstoque
