#coding: utf-8
from JTools import JToolsClass
from DadosPGM import DadosPGMClass
from PGMFile import PGMFileClass
from FileUtils import FileUtilsClass
import numpy as np

class MainClass:
    jtools = JToolsClass()
    fileUtils = FileUtilsClass()
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
        qtd_iteracoes = self.definirIteracoes()
        arr = self.fileUtils.pgmread("imagens/imagem2.pgm")
        array = self.buscarValoresDiferentes(arr)
        for a in array:
            print("COR")
            print(a.cor)
            print("LINHA")
            print(a.dadosPGM.linha)
            print("COLUNA")
            print(a.dadosPGM.coluna)
        self.fileUtils.pgmwrite(arr)
        #for contador in range(0,qtd_iteracoes):

    #255 -> preto
    #0 -> branco
    #Busca as cores diferentes e com isso os seus indices 
    # Cor
    # Linha
    # Coluna
    def buscarValoresDiferentes(self, arr):
        mylist = np.unique(arr)
        array = []
        for x in mylist:
            linha, coluna = np.where(arr == x)
            dadosPGM = DadosPGMClass(linha,coluna)
            pgmFile = PGMFileClass(x, dadosPGM)
            array.append(pgmFile)
        return array        

main = MainClass()   