class Estrada:
    def __init__ (self, length, closed, transito):
        self.length = length
        self.closed = closed # true if closed, false if open
        self.transito = transito # value between 0 and 1

    def __str__(self):
        return "Estrada: " + str(self.id) + "; Length: " + str(self.length) + "; Closed: " + str(self.closed) + "; Nodes: " + str(self.nodes)
    
    def getClosed(self):
        return self.closed
    
    def getLength(self):
        return self.length

    def getTransito(self):
        return self.transito