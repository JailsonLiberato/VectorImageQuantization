#coding: utf-8
import matplotlib.pyplot as plot 
from sklearn.cluster import KMeans
import numpy as np
from time import time
from sklearn.utils import shuffle
from sklearn.metrics import pairwise_distances_argmin
from PIL import Image
from PSO import PSOClass
from numpy import array

class KmeansClass:

    __n_colors = 64
    __pso = PSOClass()
    
    def __recriar_imagem(self, dicionario, labels, width, height):
        depth = dicionario.shape[1]
        image = np.zeros((width, height, depth))
        label_idx = 0
        for i in range(width):
            for j in range(height):
                image[i][j] = dicionario[labels[label_idx]]
                label_idx += 1
        return image

    def __recriar_imagem_PSO(self, dicionario, labels, width, height):
        depth = 3
        image = np.zeros((width, height, depth))
        label_idx = 0
        for i in range(width):
            for j in range(height):
                image[i][j] = dicionario[labels[label_idx]]
                label_idx += 1
        return image

    def executar(self, filename):
        image = Image.open(filename)
        image = np.array(image, dtype=np.float64) / 255

        #Propriedades da imagem 
        width, height, depth = tuple(image.shape)
        
        image_array = np.reshape(image, (width * height, depth))
        print(image_array.shape)

        print("Modelo de ajuste - subamostra dos dados")
        tempo_inicial = time()
        
        #Amostra de 1000
        image_array_amostra = shuffle(image_array, random_state=0)[:1000]
        kmeans = KMeans(n_clusters = self.__n_colors, random_state=0).fit(image_array_amostra)
        print("Executado em %0.3fs." % (time() - tempo_inicial))

        print("Prevê os indices de cores da imagem completa (k-means)")
        tempo_inicial = time()
        labels = kmeans.predict(image_array)
        print("Executado em %0.3fs." % (time() - tempo_inicial))


        print("Indices de cores da imagem completa (PSO/Kmeans)")
        tempo_inicial = time()
        variavel = self.__pso.execute(image_array)
        print("Executado em %0.3fs." % (time() - tempo_inicial))

        dicionario_dados_random = shuffle(image_array, random_state=0)[:self.__n_colors]
        print("Prevê os indices de cores de forma aleatória")
        tempo_inicial = time()
        labels_random = pairwise_distances_argmin(dicionario_dados_random,
                                            image_array,
                                            axis=0)
        print("Executado em %0.3fs." % (time() - tempo_inicial))

        # Display all results, alongside original image
        plot.figure(1)
        plot.clf()
        plot.axis('off')
        plot.title('Imagem original (96.615 cores)')
        plot.imshow(image)

        plot.figure(2)
        plot.clf()
        plot.axis('off')
        plot.title('Imagem quantizada (64 cores, KMeans)')
        print(kmeans.cluster_centers_)
        print(labels)
        plot.imshow(self.__recriar_imagem(kmeans.cluster_centers_, labels, width, height))

        plot.figure(3)
        plot.clf()
        plot.axis('off')
        plot.title('Imagem quantizada (64 cores, Aleatorio)')
        plot.imshow(self.__recriar_imagem(dicionario_dados_random, labels_random, width, height))

        plot.figure(4)
        plot.clf()
        plot.axis('off')
        plot.title('Imagem quantizada (K-means, PSO)')

        v = variavel
        z = np.zeros(216381)
        for w in range(len(v)):
            z[w] = int(v[w] * 255)
        clusters = array(z)
        clusters = clusters.astype(int)
        clusters = np.reshape(clusters, (-1,3))

        plot.imshow(self.__recriar_imagem(clusters, labels, width, height))

        plot.show()
    