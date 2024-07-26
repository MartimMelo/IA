import math
from rua import *
# Biblioteca de tratamento de grafos necessária para desenhar graficamente o grafo
import networkx as nx
# Biblioteca de tratamento de grafos necessária para desenhar graficamente o grafo
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, directed = False):
        self.m_nodes = []
        self.m_directed = directed
        self.m_graph = {}
        self.m_h = {}

    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out

    def getNeighbors (self, node):
        return self.m_graph[node]

    def getNodebyName (self, name):
        search_node = Rua(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
        return None
    
    def imprimeArestas(self):
        arestas = ""
        aresta = self.m_graph.keys()

        for nodo in aresta:
            for (nodo2,custo) in self.m_graph[nodo]:
                arestas = arestas + nodo.nome + " ->" + nodo2.nome + " Estrada:" + str(custo) + "\n"
        return arestas  

    def add_edge (self, nodo1, nodo2, estrada):

        if (nodo1 not in self.m_nodes):
            self.m_nodes.append(nodo1)
            self.m_graph[nodo1] = set()

        if (nodo2 not in self.m_nodes):
                    self.m_nodes.append(nodo2)
                    self.m_graph[nodo2] = set()

        self.m_graph[nodo1].add((nodo2, estrada))

        if not self.m_directed:
            self.m_graph[nodo2].add((nodo1, estrada))

    def get_arc(self, node1, node2):
        arco = None
        a = self.m_graph[node1]
        for (nodo,estrada) in a:
            if nodo == node2:
                arco = estrada
        return arco
    
    def is_closed (self, node1, node2):
        a = self.m_graph[node1]
        for (nodo,estrada) in a:
            if nodo == node2:
                return estrada.getClosed()
        return None
    
    def add_heuristica (self,n,estima):
        if n in self.m_nodes:
            self.m_h[n] = estima

    def setHeuristicas(self, end, velocidade):
        self.m_h = {}
        self.add_heuristica(end, 0)
        # pass by all nodes, begining on the end, and calculate the heuristic using the formula -> h(n) = Distance from h(n) = h(n-1) + cost(n-1,n) / velocity(n-1,n) * (1.1 - traffic(n-1,n))
        queue = [end]
        while queue:
            node = queue.pop(0)
            for (adjacente, peso) in self.m_graph[node]:
                heu = self.getH(node) + peso.getLength() / velocidade * (1.1 - peso.getTransito())
                if (adjacente not in self.m_h or heu < self.m_h[adjacente]) and peso.getClosed() == False:
                    self.add_heuristica(adjacente, heu)
                    queue.append(adjacente)

    def getH (self, node):
        if node in self.m_h:
            return self.m_h[node]
        else:
            return None

    def desenha(self):
        ##criar lista de vertices
        lista_v = self.m_nodes
        g=nx.Graph()

        #Converter para o formato usado pela biblioteca networkx
        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[nodo]:
                ad = adjacente.getName()
                g.add_edge(n,ad,weight=peso.getLength())

        #desenhar o grafo
        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()

    def calcula_tempo (self, path, velocidade):
        tempo = 0
        for i in range(len(path) - 1):
            arc = self.get_arc(path[i], path[i+1])
            tempo += arc.getLength() / velocidade * (1.1 - arc.getTransito())
        return round(tempo,2)

    def calcula_distancia (self, path):
        distancia = 0
        for i in range(len(path) - 1):
            arc = self.get_arc(path[i], path[i+1])
            distancia += arc.getLength()
        return distancia

    def depth_first (self, start, end, path=[], visited = None):
        if visited is None:
            visited = set()       
        path = path + [start]
        visited.add(start)
        if start == end:
            return path, visited
        for node in self.m_graph[start]:
            if node[0] not in visited and node[1].getClosed() == False:
                new_path, vis = self.depth_first(node[0], end, path, visited)
                if new_path:
                    return new_path, vis
        return None, None
    
    def depth_first_iterative (self, start, end, depth):
        stack = [(start, [start])]
        visited = set()
        while stack:
            (node, path) = stack.pop()
            if node not in visited:
                if len(path) > depth:
                    continue
                visited.add(node)
                if node == end:
                    return path, visited
                for next in self.m_graph[node]:
                    if next[1].getClosed() == False:
                        stack.append((next[0], path + [next[0]]))
        return None, visited

    def depth_first_limited (self, start, end):
        visited_overall = set()
        for depth in range(1, len(self.m_graph)):
            path, visited = self.depth_first_iterative(start, end, depth)
            visited_overall = visited_overall.union(visited)
            if path:
                return path, visited_overall
        return None, None

    def getvisited (self, queue):
        all_vis = [path[1] for path in queue]
        if not all_vis:
            return None
        return set(all_vis[0]).union(*all_vis[1:])

    def breadth_first (self, start, end):
        queue = [(start, [start])]
        while queue:
            (node, path) = queue.pop(0)
            for next in self.m_graph[node]:
                if next[0] not in path and next[1].getClosed() == False:
                    if next[0] == end:
                        vis = self.getvisited(queue)
                        vis.add(next[0])
                        return path + [next[0]], vis
                    else:
                        queue.append((next[0], path + [next[0]]))
        return None, None

    def uniform_cost (self, start, end):
        queue = [(start, [start], 0)]
        while queue:
            (node, path, custo) = queue.pop(0)
            for next in self.m_graph[node]:
                if next[0] not in path and next[1].getClosed() == False:
                    if next[0] == end:
                        vis = self.getvisited(queue)
                        vis.add(next[0])
                        return path + [next[0]], vis
                    else:
                        queue.append((next[0], path + [next[0]], custo + next[1].getLength()))
            queue.sort(key=lambda x: x[2])
        return None, None

    def calcula_custo (self, path):
        custo = 0
        for node in path:
            custo += self.getH(node)
        return custo

    def procuraG (self, start, end):
        open_list = set([start])
        closed_list = set([])
        parents = {}
        parents[start] = start
        visited = set()

        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or self.m_h[v] < self.m_h[n]:
                    n = v            
            if n == None:
                print ('Path does not exist!')
                return None
            
            visited.add(n)

            if n == end:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
            
                reconst_path.append(start)
                reconst_path.reverse()	

                return reconst_path, visited

            for (m, estrada) in self.getNeighbors(n):
                if m not in open_list and m not in closed_list and estrada.getClosed() == False:
                    open_list.add(m)
                    parents[m] = n
            open_list.remove(n)
            closed_list.add(n)

        print ('Path does not exist!')
        return None, None
    
    def procuraAestrela (self, start, end):
        open_list = set([start])
        closed_list = set([])
        parents = {}
        parents[start] = start
        g = {start: 0}
        visited = set()

        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or g[n] + self.getH(n) < g[n] or self.m_h[v] < self.m_h[n]:
                    n = v            
            if n == None:
                print ('Path does not exist!')
                return None
            
            visited.add(n)

            if n == end:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
            
                reconst_path.append(start)
                reconst_path.reverse()	

                return reconst_path, visited

            for (m, weight) in self.getNeighbors(n):
                if weight.getClosed() == False:
                    km = weight.getLength()
                    if m not in open_list and m not in closed_list:
                        open_list.add(m)
                        parents[m] = n
                        g[m] = g[n] + km
                    else:
                        if g[m] > g[n] + km:
                            g[m] = g[n] + km
                            parents[m] = n
                            if m in closed_list:
                                closed_list.remove(m)
                                open_list.add(m)

        print ('Path does not exist!')
        return None, None