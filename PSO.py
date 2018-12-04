#coding: utf-8
import sys
import numpy as np
import pyswarms as ps
import cv2
from pyswarms.utils.functions import single_obj as fx
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from Metrics import *
from sklearn.utils import shuffle

class PSOClass:

    kmeans = KMeans()

    def fitness(self, x, image_array):
        print("teste")
        image_array_amostra = shuffle(image_array, random_state=0)[:64]
        kmeans = KMeans(n_clusters=64, init=image_array_amostra).fit(image_array)
        silhouette_avg = silhouette_score(image_array, kmeans.labels_)
        return silhouette_avg

    def execute(self, array):
        options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
        optimizer = ps.single.GlobalBestPSO(n_particles=30, dimensions=3, options=options)
        return optimizer.optimize(self.fitness, iters=10, print_step=1, verbose=3, image_array=array)