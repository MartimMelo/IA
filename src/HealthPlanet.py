from getInput import getInput
from rua import Rua
from meioTransporte import * 
from encomenda import Encomenda
import sys

IDENCOMENDA = 0
class healthPlanet:
    def __init__(self, mapa):
        self.mapa = mapa
        self.encomendas = {}
    
    def addEncomenda(self):
        global IDENCOMENDA

        weight = 101
        while weight > 100:
            weight = getInput.getFloat("Enter the weight of the package: ")
            if weight > 100:
                print("Invalid weight!")
                
        volume = getInput.getFloat("Enter the volume of the package: ")
        time_limit = getInput.getFloat("Enter the time limit of the package: ")
        existing_address = False
        while not existing_address:
            delivery_address = input("Enter the delivery address of the package: ")
            existing_address = self.mapa.graph.getNodebyName(delivery_address)
            if not existing_address:
                print("Invalid address!")
        encomenda = Encomenda(IDENCOMENDA,weight, volume, time_limit, delivery_address)
        self.encomendas[IDENCOMENDA] = encomenda
       
        IDENCOMENDA += 1
        print("Order added!")
    
    def evaluateEncomenda(self, time, orderTime):
        if time < orderTime: 
            return 5
        else:
            avaliacao = 5 - (time - orderTime)
            if avaliacao < 0:
                return 0
            else:
                return avaliacao  

    def precoEncomenda(self, orderTime, veiculo, peso):
        preco_veiculo = MeioTransporte.calculate_preco(veiculo)
        preco = preco_veiculo * orderTime
        return round(preco  + peso * 0.3, 2)
    
    def entregarEncomenda(self):
        func_alg = {
            1 : self.mapa.graph.depth_first,
            2 : self.mapa.graph.depth_first_limited,
            3 : self.mapa.graph.breadth_first,
            4 : self.mapa.graph.uniform_cost,
            5 : self.mapa.graph.procuraG,
            6 : self.mapa.graph.procuraAestrela
        }

        print("Choose algorithm:")
        print("1. DFS")
        print("2. DFS iterative")
        print("3. BFS")
        print("4. Uniform cost")
        print("5. Greedy")
        print("6. A*")
        alg = getInput.getInt(': ')
        if alg < 1 or alg > 6:
            print("Invalid algorithm!")
            return
        
        print("Choose the package:")
        for encomenda in self.encomendas.values():
            print(encomenda)
        id = getInput.getInt(': ')
        if id not in self.encomendas:
            print("Invalid package!")
            return
        
        order = self.encomendas[id]
        objective = order.getDelivery_address()
        goal = Rua(objective)
        transport = None

        if alg < 5:
            path, visited = func_alg[alg](Rua('Central'), goal)

            possible_veicules = MeioTransporte.get_possible_veicules(order.getWeight())

            for veiculo in possible_veicules:
                vel = MeioTransporte.calculate_velocidade(veiculo, order.getWeight())
                time = self.mapa.graph.calcula_tempo(path, vel)
                if time < order.getTime_limit():
                    transport = veiculo
                    break

        else:
            possible_veicules = MeioTransporte.get_possible_veicules(order.getWeight())

            for veiculo in possible_veicules:

                vel = MeioTransporte.calculate_velocidade(veiculo, order.getWeight())
                self.mapa.graph.setHeuristicas(goal, vel)
                path, visited = func_alg[alg](Rua('Central'), goal)
                time = self.mapa.graph.calcula_tempo(path, vel)
                if time < order.getTime_limit():
                    transport = veiculo
                    break
        
        if transport == None:
            transport = possible_veicules[-1]
        
        print(f"Order delivered using {veiculo}! Time spent: {time} h")
    
        avaliacao = self.evaluateEncomenda(time, order.getTime_limit())
        print(f"Client order evaluation: {avaliacao}")

        print (f"Order price: {self.precoEncomenda(time, veiculo, order.getWeight())}")

        print(f"Path: {path}")
        print(f"Visited: {visited}")
        print(f"Km percorridos: {self.mapa.graph.calcula_distancia(path)}")

    def showMap(self):
        self.mapa.show_graph()

    def exit (self):
        print("Exiting the program!")
        sys.exit()

    def main_menu(self):
        choices = {
            "1" : self.addEncomenda,
            "2" : self.entregarEncomenda,
            "3" : self.showMap,
            "4" : self.exit
        }

        while True:
            print("Health Planet Menu:")
            print("1. Add order")
            print("2. Deliver order")
            print("3. Show Map")
            print("4. Exit")
            escolha = input("Enter your choice: ")
            if escolha in choices:
                choices[escolha]()
            else :
                print("Invalid choice!")
