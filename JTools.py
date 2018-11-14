#coding: utf-8
import os

class JToolsClass:
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
