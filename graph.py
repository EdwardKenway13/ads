#cycle in directed graph using colors recursive 

from collections import defaultdict

class Graph:


    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def dfs(self, vertex, colors):
        colors[vertex] = 'Gray'

        for v in self.graph[vertex]:

            if colors[v] == 'Gray':
                return True

            elif colors[v] == 'White' and self.dfs(v, colors) == True:
                return True

        colors[vertex] = 'Black'
        return False


    def is_cyclic(self):
        colors = ['White'] * self.vertices

        for vertex in self.graph.keys():
            if colors[vertex] == 'White':
                    if self.dfs(vertex, colors) == True:
                        return True

        return False


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print(g.is_cyclic())
