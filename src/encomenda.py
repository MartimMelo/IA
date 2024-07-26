import datetime

class Encomenda:
    def __init__(self,id, weight,volume, time_limit, delivery_address):
        self.id = id
        self.weight = weight
        self.volume = volume
        self.time_limit = time_limit
        self.delivery_address = delivery_address

    def __str__(self):
        return "Encomenda: " + str(self.id) + "; Weigth: " + str(self.weight) + "; Volume: " + str(self.volume) + "; Time Limit: " + str(self.time_limit) + "; Address: " + str(self.delivery_address)

    def getId(self):
        return id
    
    def getWeight(self):
        return self.weight

    def getVolume(self):
        return self.volume

    def getDelivery_address(self):
        return self.delivery_address
    
    def getTime_limit(self):
        return self.time_limit