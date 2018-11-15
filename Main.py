#coding: utf-8
from JTools import JToolsClass
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
        arr = self.fileUtils.pgmread("imagens/imagem.pgm")
        arr = self.buscarValoresDiferentes(arr)
        self.fileUtils.pgmwrite(arr)
        #for contador in range(0,qtd_iteracoes):

    def buscarValoresDiferentes(self, arr):
        mylist = np.unique(arr)
        arr[100] = 255
        arr[200] = 255
        arr[300] = 255
        arr[400] = 255
        return arr        
main = MainClass()   