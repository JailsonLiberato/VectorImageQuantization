#coding: utf-8
import sys
import numpy as np
import pyswarms as ps
import cv2
from pyswarms.utils.functions import single_obj as fx
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from Metrics import *

class PSOClass:

    kmeans = KMeans()

    def fitness(self, particulas):
        image = cv2.imread('imagens/globo.jpg')
        width, height, depth = tuple(image.shape)
        image_array = np.reshape(image, (width * height, depth))
        kmeans = KMeans(n_clusters=64).fit(particulas)
        resultado = Metrics.silhouette(data=image_array, centroids=kmeans.labels_)
        print(resultado)
        return resultado

    def execute(self, array):
        options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
        optimizer = ps.single.GlobalBestPSO(n_particles=30, dimensions=64, options=options)
        return optimizer.optimize(self.fitness(array), print_step=100, iters=10, verbose=3)