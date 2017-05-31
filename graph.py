import networkx as nx


def data_graph():
    G = nx.read_edgelist('data/cora.edgelist', create_using=nx.Graph())
    print(nx.info(G))
    nx.draw_networkx(G)


data_graph()
