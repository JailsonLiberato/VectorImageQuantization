#coding: utf-8
from JTools import JToolsClass
from Kmeans import KmeansClass

class MainClass:
    jtools = JToolsClass()
    kmeans = KmeansClass()
    def __init__(self):
        self.jtools.clear()
        self.executar()
    
    def definirIteracoes(self):
        condicao_saida = True
        qtd_iteracoes = 0
        while condicao_saida:
            qtd_iteracoes = raw_input("\n\nDigite a quantidade de iterações: ")
            if(qtd_iteracoes.isdigit()):
                qtd_iteracoes = int(qtd_iteracoes)
                if(qtd_iteracoes > 2 and qtd_iteracoes < 100):
                    condicao_saida = False
                else:
                    print("\n[ERRO] A quantidade deve está entre 3 e 99 iterações.")
            else:
                print("\n[ERRO] A quantidade deve está entre 3 e 99 iterações.")

        self.jtools.clear()
        return qtd_iteracoes

    def executar(self):
        print("\n\n\t\t\t\t\t::::Quantização Vetorial de Imagem::::")
        #qtd_iteracoes = self.definirIteracoes()
        self.kmeans.executar("imagens/globo.jpg")

main = MainClass()   