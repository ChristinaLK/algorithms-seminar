# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

class vertex:
    '''Object for representing vertices of graphs'''
    def __init__(self, num):
        '''initializes an instance of vertex class'''
        self.num = num
        self.edges = []
        self.parent = None
        self.kids = []
        self.distance = None
        self.color = 0
    
    def __str__(self):
        '''returns a string listing all attributes of the vertex'''
        parent_string, color_string = "None", " "
        if self.parent != None:
            parent_string = str(self.parent)
        if self.color == 0:
            color_string = "White"
        elif self.color == 1:
            color_string == "Grey"
        else: 
            color_string = "Black"
        return "Vertex: "+str(self.num)+"\nEdges: "+str(self.edges)+"\nParent: "+parent_string+"\nKids: "+str(self.kids)+"\nDistance: "+str(self.distance)#+" Color: "+color_string

# <codecell>

def graph_builder(size, edge_list):
    '''Given an integer input and a list of tuples, builds an unweighted, undirected graph'''
    graph = []
    for i in range(size+1):
        graph.append(vertex(i))
    for e in edge_list:
        start = e[0]
        end = e[1]
        graph[start].edges.append(end)
        graph[end].edges.append(start)
    return graph
    
def graph_print(graph):
    '''returns a string listing all the vertices of the graph + their attributes'''
    return_string = " "
    for v in graph[1:]:
        return_string = return_string+v.__str__()+' \n '
    return return_string

# <codecell>

def breadth_first_search(graph, source):
    '''Takes as inputs a graph represented as an adjacency list of the vertex class above
    and a source vertex.  Then cycles through the graph finding shortest paths to each vertex
    from the source vertex, changing distance/parent/kids attributes as appropriate'''
    graph[source].distance = 0
    graph[source].color = 1
    queue = []
    queue.append(source)
    while len(queue) != 0:
        #print queue
        v = queue.pop(0)
        for e in graph[v].edges:
            if graph[e].color == 0:
                graph[e].color = 1
                graph[e].parent = v
                graph[v].kids.append(e)
                graph[e].distance = graph[v].distance + 1
                queue.append(e)
        graph[v].color = 2  

# <codecell>

##Sample input, printed output

sample_edges = [ (1,2), (1,3), (2,4), (3,4), (3,5), (3,7), (4,5), (4,6)]

sample_graph = graph_builder(7, sample_edges)

print graph_print(sample_graph)

# <codecell>

##Output after BFS with source 2

breadth_first_search(sample_graph, 2)

print graph_print(sample_graph)

# <codecell>

##function to plot the shortest paths tree

import numpy as np
import matplotlib.pyplot as plt

%pylab inline

def treeplot(graph, source):
    fig, ax = plt.subplots()
    axx = float(4)
    axy = float(4)
    plt.axis('off')
 
    
    def plotchildren(vertex,distance,xparent,yparent):
        item = str(vertex.num)
        ax.text(xparent,yparent, item, fontsize=15)
        #num_kids = len(vertex.kids)
        xkid = xparent
        ykid = yparent - 0.4
        for k in vertex.kids:
            xkid = xkid + axx/2**distance
            plotchildren(graph[k],graph[k].distance,xkid,ykid)
            ax.plot([xparent,xkid],[yparent,ykid],color='blue')
        
    number = 1
    xparent = axx/2
    yparent = axy
    plotchildren(graph[source],graph[source].distance,xparent,yparent)

# <codecell>

treeplot(sample_graph, 2)

# <codecell>


# <codecell>


