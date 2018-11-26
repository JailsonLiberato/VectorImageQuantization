#coding: utf-8
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_sample_image
import numpy as np
from time import time
from sklearn.utils import shuffle
from sklearn.metrics import pairwise_distances_argmin
from PIL import Image

class KmeansClass:

    n_colors = 64
    
    def recreate_image(self, codebook, labels, w, h):
        d = codebook.shape[1]
        image = np.zeros((w, h, d))
        label_idx = 0
        for i in range(w):
            for j in range(h):
                image[i][j] = codebook[labels[label_idx]]
                label_idx += 1
        return image

    def executar(self, filename):
        image = Image.open(filename)
        image = np.array(image, dtype=np.float64) / 255
        print(image.shape)
        
        #Propriedades da imagem 
        width, height, d = tuple(image.shape)
        print(width)
        print(height)
        print(d)
        
        image_array = np.reshape(image, (width * height, d))
        print("Fitting model on a small sub-sample of the data")
        t0 = time()
        image_array_sample = shuffle(image_array, random_state=0)[:1000]
        kmeans = KMeans(n_clusters = self.n_colors, random_state=0).fit(image_array_sample)
        print("done in %0.3fs." % (time() - t0))

        # Get labels for all points
        print("Predicting color indices on the full image (k-means)")
        t0 = time()
        labels = kmeans.predict(image_array)
        print("done in %0.3fs." % (time() - t0))

        codebook_random = shuffle(image_array, random_state=0)[:self.n_colors]
        print("Predicting color indices on the full image (random)")
        t0 = time()
        labels_random = pairwise_distances_argmin(codebook_random,
                                            image_array,
                                            axis=0)
        print("done in %0.3fs." % (time() - t0))

        # Display all results, alongside original image
        plt.figure(1)
        plt.clf()
        plt.axis('off')
        plt.title('Original image (96,615 colors)')
        plt.imshow(image)

        plt.figure(2)
        plt.clf()
        plt.axis('off')
        plt.title('Quantized image (64 colors, K-Means)')
        plt.imshow(self.recreate_image(kmeans.cluster_centers_, labels, width, height))

        plt.figure(3)
        plt.clf()
        plt.axis('off')
        plt.title('Quantized image (64 colors, Random)')
        plt.imshow(self.recreate_image(codebook_random, labels_random, width, height))
        plt.show()

    