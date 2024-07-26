BICICLETA = "Bike"
MOTO = "Motorcycle"
CARRO = "Car"


class MeioTransporte:

    def get_possible_veicules(weight_encomenda):
        if weight_encomenda <= 10:
            return [BICICLETA, MOTO, CARRO]
        elif weight_encomenda <= 20:
            return [MOTO, CARRO]
        else:
            return [CARRO]

    def calculate_velocidade(veiculo, weight_encomenda):
        if veiculo == BICICLETA:
            return 10 - weight_encomenda * 0.6
        elif veiculo == MOTO:
            return 20 - weight_encomenda * 0.5
        elif veiculo == CARRO:
            return 30 - weight_encomenda * 0.1
        
    def calculate_preco(veiculo):
        if veiculo == BICICLETA:
            return 2
        elif veiculo == MOTO:
            return 10
        elif veiculo == CARRO:
            return 20
        