import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
from itertools import groupby
import collections

# draw degree distribution for n = 100, 1000, 10000
def drawDD(G1, G2, G3):
    #G1
    degree_sequence_1 = sorted([d for n, d in G1.degree()], reverse=True)  # degree sequence
    degreeFrequency_1 = [len(list(group)) for key, group in groupby(degree_sequence_1)]
    distinctDegree_1 = list(set(degree_sequence_1))
    intermediate_degree_dist_1 = zip(distinctDegree_1 , degreeFrequency_1)
    print intermediate_degree_dist_1

    #G2
    degree_sequence_2 = sorted([d for n, d in G2.degree()], reverse=True)  # degree sequence
    degreeFrequency_2 = [len(list(group)) for key, group in groupby(degree_sequence_2)]
    distinctDegree_2 = list(set(degree_sequence_2))
    intermediate_degree_dist_2 = zip(distinctDegree_2, degreeFrequency_2)
    print intermediate_degree_dist_2

    #G3
    degree_sequence_3 = sorted([d for n, d in G3.degree()], reverse=True)  # degree sequence
    degreeFrequency_3 = [len(list(group)) for key, group in groupby(degree_sequence_3)]
    distinctDegree_3 = list(set(degree_sequence_3))
    intermediate_degree_dist_3 = zip(distinctDegree_3, degreeFrequency_3)
    print intermediate_degree_dist_3


    plt.plot(distinctDegree_1,degreeFrequency_1,'bo',distinctDegree_2,degreeFrequency_2,'g^',distinctDegree_3,degreeFrequency_3,'r*',linewidth=2.0, ms = 12)
    plt.ylabel('degreeFrequency')
    plt.xlabel('distinctDegree')
    plt.axes([0.45,0.45,0.45,0.45])
    plt.axis('off')
    plt.show()
# draw cumulative degree distribution for n
def drawCDD(G1, G2, G3):
    #G1
    degree_sequence_1 = sorted([d for n, d in G1.degree()], reverse=True)
    degreeFrequency_1 = [len(list(group)) for key, group in groupby(degree_sequence_1)]
    distinctDegree_1 = list(set(degree_sequence_1))
    x = 0
    cdd_1 = []
    while x < len(degreeFrequency_1):
        cdd_1.append(sum(degreeFrequency_1[0:x]))
        x += 1


    #G2
    degree_sequence_2 = sorted([d for n, d in G2.degree()], reverse=True)
    degreeFrequency_2 = [len(list(group)) for key, group in groupby(degree_sequence_2)]
    distinctDegree_2 = list(set(degree_sequence_2))
    x = 0
    cdd_2 = []
    while x < len(degreeFrequency_2):
        cdd_2.append(sum(degreeFrequency_2[0:x]))
        x += 1

    #G3
    degree_sequence_3 = sorted([d for n, d in G3.degree()], reverse=True)
    degreeFrequency_3 = [len(list(group)) for key, group in groupby(degree_sequence_3)]
    distinctDegree_3 = list(set(degree_sequence_3))
    x = 0
    cdd_3 = []
    while x < len(degreeFrequency_3):
        cdd_3.append(sum(degreeFrequency_3[0:x]))
        x += 1


    plt.loglog(distinctDegree_1,cdd_1,'bo',distinctDegree_2,cdd_2,'g^',distinctDegree_3,cdd_3,'r*',linewidth=2.0, ms = 12)
    plt.ylabel('cumulative degree')
    plt.xlabel('distinctDegree')
    plt.axes([0.45,0.45,0.45,0.45])
    plt.axis('off')
    plt.show()

# draw barabasi_albert_model for n = 10000
def barabasi_albert_generator(n, m):

    G = nx.complete_graph(m)
    targets = list(range(m))
    repeated_nodes = []
    NumOfNodes = m
    degree = []
    g1 = nx.empty_graph()
    g2 = nx.empty_graph()
    g3 = nx.empty_graph()
    k1 =[]
    k2 =[]
    k3 =[]

    G_node = G.nodes()

    beta = 1 / 2
    while NumOfNodes < n:
        # Add edges to m nodes
        G.add_edges_from(zip([NumOfNodes]*m,targets))
        repeated_nodes.extend(targets)
        repeated_nodes.extend([NumOfNodes]*m)
        targets = random.sample(repeated_nodes, m)
        NumOfNodes += 1

    #  graphs with n = 100, 1000, 10000 in intermediate steps
        if NumOfNodes == 100:

            k1.append(m*(NumOfNodes/m)**beta)
            g1 = G.copy()
        if  NumOfNodes == 1000:

            k2.append(m*(NumOfNodes/m)**beta)
            g2 = G.copy()
        if  NumOfNodes == 10000:

            k3.append(m*(NumOfNodes/m)**beta)
            g3 = G.copy()

    print 'TEST:' ,k1,k2,k3
    ##print 'TEST:', min(list(d for i, d in g1.degree()))
    drawCDD(g1, g2, g3)
    #drawDD(g1, g2, g3)
    ##print 'TEST:', min(list(d for i, d in g1.degree()))



    GBa = nx.barabasi_albert_graph(10000, 4)
    dgs = [d for i, d in GBa.degree()]
    cds = np.zeros(max(dgs) + 1)
    for d in dgs: cds[d] += 1
    plt.loglog(cds / float(sum(cds)), '.m')

    # plt.loglog(YOUR_DEGREE_DIST,'.c')

    plt.title('TEST-TEST-BA')
    plt.show()

    return G
# run Graph_generator

generatedG = barabasi_albert_generator(10000,4)


#print clustering coefficient of g
print "Average Clusterin Coefficient = ",nx.average_clustering(generatedG)




