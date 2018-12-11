#coding: utf-8
from JTools import JToolsClass
from Kmeans import KmeansClass

class MainClass:
    
    __jtools = JToolsClass()
    __kmeans = KmeansClass()

    def __init__(self):
        self.__jtools.clear()
        self.__executar()

    def __executar(self):
        print("\n\n\t\t\t\t\t::::Quantização Vetorial de Imagem::::")
        self.__kmeans.executar("imagens/globo.jpg")

main = MainClass()   