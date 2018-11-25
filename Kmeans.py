#coding: utf-8
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.cluster import KMeans

class KmeansClass:

    def executar(self):
        iris = pd.read_csv("arquivos/iris.csv")
        x = iris.iloc[:, 0:4].values
        kmeans = KMeans(n_clusters = 3, init = 'random')
        kmeans.fit(x)
        distance = kmeans.fit_transform(x)
        labels = kmeans.labels_
        print(labels)
        wcss = []
 
        for i in range(1, 11):
            kmeans = KMeans(n_clusters = i, init = 'random')
            kmeans.fit(x)
            print i,kmeans.inertia_
            wcss.append(kmeans.inertia_)  
        #Plotar uma curva
        #plt.plot(range(1, 11), wcss)
        #plt.title('O Metodo Elbow')
        #plt.xlabel('Numero de Clusters')
        #plt.ylabel('WSS') #within cluster sum of squares
        #plt.show()

        data = [
        [ 4.12, 3.4, 1.6, 0.7],
        [ 5.2, 5.8, 5.2, 6.7],
        [ 3.1, 3.5, 3.3, 3.0]
        ]
        kmeans.predict(data)


        #Exibir os centroides.
        plt.scatter(x[:, 0], x[:,1], s = 100, c = kmeans.labels_)
        plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'red',label = 'Centroides')
        plt.title('Iris Clusters and Centroids')
        plt.xlabel('SepalLength')
        plt.ylabel('SepalWidth')
        plt.legend()
 
        plt.show()