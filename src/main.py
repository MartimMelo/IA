from Mapa import Mapa
from rua import Rua
from HealthPlanet import healthPlanet 
from estrada import Estrada 

def generate_map():
    # ! Initial state's streets
    central = Rua('Central')
    rua_1 = Rua('Rua 1')
    rua_2 = Rua('Rua 2')
    rua_3 = Rua('Rua 3')
    rua_4 = Rua('Rua 4')
    rua_5 = Rua('Rua 5')
    rua_6 = Rua('Rua 6')
    rua_7 = Rua('Rua 7')
    rua_8 = Rua('Rua 8')
    rua_9 = Rua('Rua 9')
    rua_10 = Rua('Rua 10')
    rua_11 = Rua('Rua 11')
    rua_12 = Rua('Rua 12')
    rua_13 = Rua('Rua 13')
    rua_14 = Rua('Rua 14')
    rua_15 = Rua('Rua 15')
    rua_16 = Rua('Rua 16')
    rua_17 = Rua('Rua 17')
    rua_18 = Rua('Rua 18')
    rua_19 = Rua('Rua 19')

    ruas = [central, rua_1, rua_2, rua_3, rua_4, rua_5, rua_6, rua_7, rua_8, rua_9, rua_10, rua_11, rua_12, rua_13, rua_14, rua_15, rua_16, rua_17, rua_18, rua_19]
    initial_state = Mapa(ruas)
    
    initial_state.graph.add_edge(central, rua_5, Estrada(5, False, 0.3))
    initial_state.graph.add_edge(central, rua_7, Estrada(3, False, 0.2))
    initial_state.graph.add_edge(central, rua_11, Estrada(7, True, 0.2))
    initial_state.graph.add_edge(central, rua_13, Estrada(4, False, 0.2))
    initial_state.graph.add_edge(central, rua_16, Estrada(4, False, 0.1))

    initial_state.graph.add_edge(rua_5, rua_3, Estrada(1, False, 0.2))
    initial_state.graph.add_edge(rua_5, rua_4, Estrada(1, False, 0.6))
    initial_state.graph.add_edge(rua_3, rua_1, Estrada(3, True, 0.6))
    initial_state.graph.add_edge(rua_4, rua_2, Estrada(1, False, 0.5))
    initial_state.graph.add_edge(rua_2, rua_1, Estrada(2, False, 0.3))
    initial_state.graph.add_edge(rua_4, rua_3, Estrada(1, False, 0.8))

    initial_state.graph.add_edge(rua_3, rua_19, Estrada(5, False, 0.1))

    initial_state.graph.add_edge(rua_19, rua_18, Estrada(3, False, 0.4))
    initial_state.graph.add_edge(rua_18, rua_17, Estrada(1, False, 0.6))
    initial_state.graph.add_edge(rua_18, rua_16, Estrada(2, False, 0.4))
    initial_state.graph.add_edge(rua_16, rua_17, Estrada(1, False, 0.3))

    initial_state.graph.add_edge(rua_17, rua_15, Estrada(7, False, 0.2))
    initial_state.graph.add_edge(rua_16, rua_13, Estrada(5, False, 0.2))

    initial_state.graph.add_edge(rua_13, rua_15, Estrada(1, False, 0.3))
    initial_state.graph.add_edge(rua_13, rua_14, Estrada(2, False, 0.4))
    initial_state.graph.add_edge(rua_13, rua_12, Estrada(1, False, 0.4))
    initial_state.graph.add_edge(rua_14, rua_12, Estrada(2, False, 0.2))

    initial_state.graph.add_edge(rua_12, rua_11, Estrada(4, False, 0.2))
    initial_state.graph.add_edge(rua_11, rua_10, Estrada(2, False, 0.1))

    initial_state.graph.add_edge(rua_10, rua_9, Estrada(4, False, 0.1))

    initial_state.graph.add_edge(rua_9, rua_7, Estrada(2, False, 0.1))
    initial_state.graph.add_edge(rua_9, rua_8, Estrada(2, False, 0.1))
    initial_state.graph.add_edge(rua_7, rua_6, Estrada(1, False, 0.2))
    initial_state.graph.add_edge(rua_8, rua_6, Estrada(1, False, 0.2))

    initial_state.graph.add_edge(rua_6, rua_4, Estrada(3, False, 0.3))

    return initial_state

def main():
    inicial_state = generate_map()

    health_planet = healthPlanet(inicial_state)
    health_planet.main_menu()

if __name__ == "__main__":
    main() 