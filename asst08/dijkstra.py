# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

class vertex:
    '''Vertex object to represent vertex of a graph.  The color attribute is used to 
    track whether a vertex has been "discovered" in the search for a shortest path.  
    I have used "None" to indicate infinite distance'''
    def __init__(self, num):
        '''Initializes object instance with numerical label of vertex'''
        self.num = num
        self.edges = []
        self.parent = None
        self.kids = []
        self.distance = None
        self.color = False
    
    def find_edgeweight(self, edge):
        '''find the weight for an edge from this vertex to a vertex with numerical label edge'''
        for e in self.edges:
            if e.num == edge:
                return e.weight
        return None
    
    def __str__(self, mode="short"):
        '''Returns a string listing attributes of a vertex'''
        parent_string, edges_string, color_string = "None", " " , " "
        if self.parent != None:
            parent_string = str(self.parent.num)
        if self.edges != []:
            for e in self.edges:
                edges_string = edges_string+str(e.num)+", "
        if self.color:
            color_string = "Black"
        else:
            color_string = "White"
        return "Vertex: "+str(self.num)+" Parent: "+parent_string+" Distance: "+str(self.distance)+" Color: "+color_string+" Edges are: "+edges_string

# <codecell>

class edge:
    '''Edge object to represent edge of a graph, attributes include numerical label,
    "pointer" to the destination vertex, and weight of the edge'''
    def __init__(self, val, dest_vertex = None, weight=1):
        '''Creates an instance of an edge, required input is numerical label,
        optional inputs are the destination vertex and weight of the edge'''
        self.num = val
        self.dest = dest_vertex
        self.weight = weight

# <codecell>

class graph:
    '''Represents a graph using an adjacency list of vertices.  The "extra set" attribute
        is a list of the vertex labels, and is used later to run dijkstra's algorithm - it 
        essentially tracks which vertices have not yet joined the "shortest path" set'''
    def __init__(self, num, edge_list):
        '''Initialize the graph by creating a list of vertices of length "size" and 
        then adding each edge from the edge_list to the "edges" attribute of the appropriate
        vertex.  Each edge is a tuple formatted as ((v1,v2),weight)'''
        self.size = num+1
        self.extra_set = range(1,num+1)
        self.vertices = []
        for i in range(self.size):
            self.vertices.append(vertex(i))
        for e in edge_list:
            start_vertex = e[0][0]
            end_vertex = e[0][1]
            weight = e[1]
            self.vertices[start_vertex].edges.append(edge(end_vertex, self.vertices[end_vertex], weight))                

    def find_min(self):
        '''of the vertices remaining in the attribute "extra_set", finds the vertex 
        with the smallest distance attribute'''
        assert self.extra_set != [], "Set to be minimized is non-empty"
        initial= self.extra_set[0]
        smallest_distance = self.vertices[initial].distance
        return_vertex = self.vertices[initial]
        for index in self.extra_set:
            if self.vertices[index].distance < smallest_distance:
                smallest_distance = self.vertices[index].distance
                return_vertex = self.vertices[index]
        return return_vertex
    
    def relax(self, v):
        '''explores all vertices in the edge set of v (destinations from v) and updates their
        shortest distance if appropriate.  This step is done after v.distance is optimized already.'''
        if v.distance != None:  #intermediate vertex must be discovered already
            for e in v.edges:  #go through each edge
                u = e.dest
                if u.color is not True:  #if the element is not yet "discovered"
                    u.distance = v.distance + e.weight
                    u.color = True
                    #print "changed path from ",v.num,"to",u.num,"new distance is",u.distance
                elif u.distance > v.distance + e.weight: #if the new path is better
                    u.distance = v.distance + e.weight
                    u.parent = v
                    #print "changed path from ",v.num,"to",u.num,"new distance is",u.distance
    
    def __str__(self):
        '''returns a string containing all vertices of the graph + their attributes'''
        return_string = " "
        for v in self.vertices[1:]:
            return_string = return_string+v.__str__()+' \n '
        return_string = return_string+str(self.extra_set)
        return return_string

# <codecell>

##test graph (from: http://faculty.ycp.edu/~dbabcock/cs360/lectures/lecture21.html)

test_edges = [((1,3),6 ), ((1,4),3 ),  ((2,1), 3),  ((3,4), 2),  ((4,2), 1), ((4,3), 1), ((5,2), 4), ((5,4), 2)]

test_graph = graph(5, test_edges)

print test_graph

# <codecell>

def dijkstra(g, source):
    '''Takes a graph and the number of a source vertex as inputs, 
    runs dijkstra's algorithm for shortest paths, modifying attributes
    of the vertices as appropriate'''
    v_source = g.vertices[source]
    v_source.color = True
    v_source.distance = 0
    g.relax(v_source)
    g.extra_set.remove(source)
    while g.extra_set != []:
        v = g.find_min()
        #v.parent.kids.append(v.num)
        g.relax(v)
        g.extra_set.remove(v.num)

# <codecell>

##run dijkstra on the test graph

dijkstra(test_graph, 5)
print test_graph

# <codecell>


