from graph import Graph

class Mapa:

    def __init__(self, ruas):
        self.graph = Graph()
        self.ruas = ruas

    def create_graph(self):
        self.graph = Graph()
        for rua in self.ruas:
            self.graph.add_node(rua.nome)

    def print_graph(self):
        print(self.graph)
        print(self.graph.imprimeArestas())

    def show_graph(self):
        self.graph.desenha()