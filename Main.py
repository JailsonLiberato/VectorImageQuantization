#coding: utf-8
import cv2
import numpy as np
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from JTools import JToolsClass
from Kmeans import KmeansClass

class MainClass:
    
    jtools = JToolsClass()
    kmeans = KmeansClass()

    def __init__(self):
        self.jtools.clear()
        self.executar()

    def executar(self):
        print("\n\n\t\t\t\t\t::::Quantização Vetorial de Imagem::::")
        self.kmeans.executar("imagens/globo.jpg")

main = MainClass()   