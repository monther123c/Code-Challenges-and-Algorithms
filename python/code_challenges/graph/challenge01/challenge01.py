# Write here the code challenge solution
class Node:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self,value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex

    def add_edge(self,node1,node2,weight=0):
        
        if not node1 in self.adj_list.keys():
            return("this node does not exist")

        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2,weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1,weight)
        self.adj_list[node2].append(edge2)

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output+= f'{vertex} ->'
            for edge in self.adj_list[vertex]:
                output+= f'{edge.vertex} ---> '
            output+= '\n'
        return output
    def BreadthFirst(self,root):
        '''
        type: root --> start point
        rtype: list --> all nodes
        '''
        nodes = []
        queue  = []
        visited = set()
        queue.append(root)
        visited.add(root)
        while queue:
            start = queue.pop(0)
            nodes.append(start.value)
        
            for i in self.adj_list[start]:
                if i.vertex not in visited:
                    queue.append(i.vertex)
                    visited.add(i.vertex)
        
        return nodes
        
if __name__ == "__main__":

    test = Graph()
    a = test.add_node('A')
    b = test.add_node('B')
    c = test.add_node('C')
    d = test.add_node('D')
    e = test.add_node('E')
    f = test.add_node('F')
    g = test.add_node('G')
    h= test.add_node('H')
    i= test.add_node('I')
    k= test.add_node('K')

    test.add_edge(a,c)
    test.add_edge(a,e)
    test.add_edge(a,b)
    test.add_edge(c,f)
    test.add_edge(b,d)
    test.add_edge(e,g)
    test.add_edge(e,d)
    test.add_edge(e,f)
    test.add_edge(f,i)
    test.add_edge(g,h)
    test.add_edge(f,h)
    test.add_edge(i,k)
    test.add_edge(h,k)

    print(test)
    
    print(test.BreadthFirst(a))