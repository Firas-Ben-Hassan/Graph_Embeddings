from sklearn.cluster import KMeans
import numpy as np
from gensim.models import KeyedVectors


def cluster_node_features():
    node_features_file = input("Enter feature vectors file: ")
    node_features = KeyedVectors.load_word2vec_format(node_features_file)

    N = int(input("Enter number of nodes: "))
    X = []
    notX = []
    for i in range(1, N + 1):
        try:
            X.append(np.array(node_features[str(i)]))
        except:
            notX.append(i)

    n_clusters = int(input("Enter no. of clusters: "))
    kmeans = KMeans(n_clusters=n_clusters).fit(X)

    for i in notX:
        X.insert(i - 1, None)

    clusters_output_file = input("Enter output file: ")
    with open(clusters_output_file, 'w') as out:
        cf = [str(N) + " " + str(n_clusters) + "\n"]
        for i in range(N):
            try:
                cl = [0] * n_clusters
                cl[kmeans.predict(X[i].reshape(1, -1))[0]] = 1
                cn = [i + 1] + cl
                cf.append(" ".join([str(n) for n in cn]) + "\n")
            except:
                cl = [0] * n_clusters
                cn = [i + 1] + cl
                cf.append(" ".join([str(n) for n in cn]) + "\n")
        out.writelines(cf)

    graph_output_file = input("Enter graph file: ")
    with open(graph_output_file, 'w') as out:
        for i in range(N):
            try:
                cl = [kmeans.predict(X[i].reshape(1, -1))[0]]
                cn = [i + 1] + cl
                cf.append(" ".join([str(n) for n in cn]) + "\n")
            except:
                cl = [n_clusters]
                cn = [i + 1] + cl
                cf.append(" ".join([str(n) for n in cn]) + "\n")
        out.writelines(cf)

if __name__ == "__main__":
    cluster_node_features()
