#coding: utf-8
from pyswarm import pso
import sys
import numpy as np
import pyswarms as ps
import cv2
from pyswarms.utils.functions import single_obj as fx
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.utils import shuffle
from PIL import Image
import numpy as np 

class PSOClass:

    kmeans = KMeans()
    image = Image.open("imagens/globo.jpg")
    image = np.array(image, dtype=np.float64) / 255
    #Propriedades da imagem 
    width, height, depth = tuple(image.shape)
    image_array = np.reshape(image, (width * height, depth))
    image_array_amostra = shuffle(image_array, random_state=0)[:2]

    def fitness(self, x, y):
        #kmeans = KMeans(n_clusters=64, n_init=1, init=self.image_array_amostra).fit(self.image_array)
        #print(kmeans.labels_)
        ##silhouette_avg = silhouette_score(self.image_array, kmeans.labels_)
        #print(silhouette_avg)
        #return np.linalg.norm(self.image_array - self.image_array_amostra, axis=-1).sum()
        #kmeans = KMeans(n_clusters=2,init=self.image_array_amostra).fit(self.image_array)
        #silh=(-1)*silhouette_score(self.image_array,kmeans.labels_)
        #return silh
        coeffs=[]
        kmeans = KMeans(n_clusters=64).fit(self.image_array)
        sil_coeff = silhouette_score(self.image_array, kmeans.labels_,metric='euclidean')
        coeffs.append(sil_coeff)
        coeffs=np.array(coeffs)  
        print(coeffs)
        return coeffs
    
    def execute(self, array):
        options = {'c1': 0.9, 'c2': 0.9, 'w':1.9}
        optimizer = ps.single.GlobalBestPSO(n_particles=30, dimensions=3, options=options)
        cost, pos = optimizer.optimize(self.fitness, 1, print_step=1, verbose=3, y=1)
        print(cost)
        print(pos)
        return pos