import XNode2Vec as xn2v
import numpy as np
import networkx as nx

G = np.load('ComunityNetwork.npy')
G = nx.from_numpy_matrix(G)
walk_l = 50
p, q = 0.1, 0.9
starting_node = 4
nodes, similarity = xn2v.n2v_algorithm(G, starting_node, picked = 6,
                                  dim=128, walk_length=walk_l,
                                  context=100, p=p, q=q, Weight = False,
                                  workers=4, train_time = 5)
nodes = np.append(nodes, starting_node)
xn2v.Draw(G, nodes)
