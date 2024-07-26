class Rua:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome

    def getName(self):
        return self.nome

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Rua):
            return False
        return self.nome == other.nome 

    def __hash__(self):
        return hash(self.nome)
    
    def getName(self):
        return self.nome