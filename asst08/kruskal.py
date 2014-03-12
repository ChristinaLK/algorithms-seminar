# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

class edge:
    '''edge object for representing graphs, contains input/output vertex attributes,
    weight attribute and boolean toggle for inclusion in min spanning tree'''
    def __init__(self,first,second,weight):\
        '''initializes an instance of the edge, 3 inputs: the 2 vertices of the edge and an edge weight'''
        self.u = first
        self.v = second
        self.weight = weight
        self.chosen = False
        
    def __str__(self):
        '''returns a string listing attributes of the edge'''
        return_string = "("+str(self.u)+", "+str(self.v)+")"+" Weight: "+str(self.weight)
        return return_string

# <codecell>

##sample edge
e = edge(1,2,3)
print e

# <codecell>

class vertex:
    '''Vertex object '''
    def __init__(self, num):
        '''initializes an instance of a vertex.  tree attribute will be used for determining which
        vertices are already part of a tree.  one input: the numeric label of the vertex'''
        self.num = num
        self.edges = []
        self.tree = None
    
    def __str__(self):
        '''returns a string containing attributes of the vertex'''
        return_string = "Vertex: "+str(self.num)+", Edges: "+str(self.edges)
        return return_string

# <codecell>

##sample vertex
v = vertex(2)
v.edges.append(3)
v.edges.append(5)
print v

# <codecell>

class kruskal:
    '''a modified graph object, with methods related to using kruskal's algorithm'''
    def __init__(self, size, edges_list):
        '''initializes an (undirected) graph, based on size and a list of edges.  List of edges
        is sorted by weight first to save time later on.  edges are tuples in the format 
        (v1, v2, weight)'''
        edges_list = sorted(edges_list, key=lambda edge: edge[2])
        self.size = size + 1
        self.vertices = []  
        self.edges = []   
        self.tree_number = 0
        for i in range(self.size):
            self.vertices.append(vertex(i))
        for e in edges_list:
            u = e[0]
            v = e[1]
            w = e[2]
            self.vertices[u].edges.append(v)
            self.vertices[v].edges.append(u)
            self.edges.append(edge(u,v,w))
    
    def update_tree(self,u,v):
        '''Called when adding edge (u,v) connects two previously disjoint trees in the
        min-spanning tree.  Updates all vertices with v's tree number to u's tree number'''
        old_tree = v.tree
        new_tree = u.tree
        for vertex in self.vertices:
            if vertex.tree == old_tree:
                vertex.tree = new_tree
    
    def cycle_check(self,u,v):
        '''checks if adding the edge (u,v) to the min-spanning tree will create a cycle.  
        If a cycle is created, returns False.  If a cycle is not created, sets the tree
        attribute of each vertex as appropriate and returns True'''
        uu = self.vertices[u]
        vv = self.vertices[v]
        if uu.tree is None and vv.tree is None:  ##neither verttex is connected to the min-spanning tree, creates a new tree
            uu.tree = vv.tree = self.tree_number
            self.tree_number+=1
            return True
        elif vv.tree is None:  ##one vertex is not connected, connect it to uu's tree
            vv.tree = uu.tree
            return True
        elif uu.tree is None:  ##reverse of above
            uu.tree = vv.tree
            return True
        elif uu.tree != vv.tree:  ##both are connected, but to different trees.  Add edge, update tree numbers
            self.update_tree(uu,vv)
            return True
        else: 
            return False
    
    def min_spanning(self):
        '''implements kruskal's algorithm for finding a min-spanning tree by cycling through the list
        of edges (already sorted in order of weight), changing their chosen attribute to True if adding
        the edge doesn't create a cycle.  Prints chosen edges after algorithm terminates.'''
        for e in self.edges:
            if self.cycle_check(e.u,e.v):
                e.chosen = True
        for e in self.edges:
            if e.chosen:
                print e
    
    def __str__(self):
        '''returns a string representing all vertices + edges of the graph with their attributes'''
        v_string, e_string = " ", " "
        for v in self.vertices:
            v_string = v_string + v.__str__() + "\n"
        for e in self.edges:
            e_string = e_string + e.__str__() + "\n"
        return v_string + "\n" + e_string


# <codecell>

##Test graph #1 

test_edges = [ (3,5,6), (3,4,2), (2,5,4), (1,2,3),  (2,3,5), (4,5,7), (1,5,1)]

test_graph = kruskal(5, test_edges)

print test_graph

test_graph.min_spanning()

# <codecell>

##Test graph #2

wiki_edges = [(1,4,5),(1,2,7),(2,4,9),(2,3,8),(2,5,7),(3,5,5),(4,5,15),(4,6,6),(5,6,8),(6,7,11),(5,7,9)]
wiki_graph = kruskal(7,wiki_edges)
print wiki_graph

wiki_graph.min_spanning()

# <codecell>


