import numpy as np
import pandas as pd
import networkx as nx
from Xnode2vec import complete_edgelist, stellar_edgelist, generate_edgelist
import pytest

def test_complete_dimension():
    """
    Checks if the length of the edgelist generated by complete_edgelist() is equal to the number of points of the
    dataset squared.
    """
    rows = np.random.randint(1,30)
    columns = np.random.randint(1,30)
    dataset = np.random.rand(rows,columns)
    assert len(complete_edgelist(dataset).index) == dataset.shape[0]**2

def test_stellar_dimension():
    """
    Checks if the length of the edgelist generated by stellar_edgelist() is equal to the number of points of the
    dataset.
    """
    rows = np.random.randint(1,30)
    columns = np.random.randint(1,30)
    dataset = np.random.rand(rows,columns)
    assert len(stellar_edgelist(dataset).index) == dataset.shape[0]

def test_complete_zeroweight():
    """
    Checks if the weights of a dataset with zero distance between all the points is 1.
    """
    rows = np.random.randint(1, 30)
    columns = np.random.randint(1, 30)
    dataset = np.zeros((rows, columns))
    assert complete_edgelist(dataset).loc[:,'weight'].values.all() == 1.

def test_stellar_zeroweight():
    """
    Checks the data types of the produced list for the stellar_edgelist function.
    """
    rows = np.random.randint(1, 30)
    columns = np.random.randint(1, 30)
    dataset = np.zeros((rows, columns))
    assert complete_edgelist(dataset).loc[:,'weight'].values.all() == 1.

def test_complete_checktypes():
    """
    Checks the data types of the produced list for the complete_edgelist() function.
    """
    rows = np.random.randint(1, 30)
    columns = np.random.randint(1, 30)
    dataset = np.zeros((rows, columns))
    df = complete_edgelist(dataset)
    assert (all(isinstance(item, str) for item in df['node1'].values),
            all(isinstance(item, str) for item in df['node2'].values),
            all(isinstance(item, float) for item in df['weight'].values)) == (True,True,True)

def test_stellar_checktypes():
    """
    Checks the data types of the produced list for the stellar_edgelist() function.
    """
    rows = np.random.randint(1, 30)
    columns = np.random.randint(1, 30)
    dataset = np.zeros((rows, columns))
    df = stellar_edgelist(dataset)
    assert (all(isinstance(item, str) for item in df['node1'].values),
            all(isinstance(item, str) for item in df['node2'].values),
            all(isinstance(item, float) for item in df['weight'].values)) == (True, True, True)

def test_nxedgelist_samenode():
    """
    Checks if inserting the same point will produce a network of dimension 1.
    """
    rows = np.random.randint(1, 30)
    narray = np.ones((rows, 3))
    df = pd.DataFrame(narray, columns = ['node1', 'node2', 'weight'])
    df = generate_edgelist(df)
    G = nx.Graph()
    G.add_weighted_edges_from(df)
    assert len(list(G.nodes)) == 1
