class Station(object):
    gas_amount = 100

    def refill(self, car):
        if car.gas_amount > 0:
            self.gas_amount -= (car.capacity - car.gas_amount)
            car.gas_amount += (car.capacity - car.gas_amount)
            return self.gas_amount
        else:
            self.gas_amount -= car.capacity
            car.gas_amount += car.capacity
            return self.gas_amount


class Car(object):

    def __init__(self, gas_amount=0, capacity=100):
        self.gas_amount = gas_amount
        self.capacity = capacity


JR_Petrol = Station()
mustang = Car(10)
print(JR_Petrol.gas_amount)
print(mustang.gas_amount, mustang.capacity)
JR_Petrol.refill(mustang)
print(JR_Petrol.gas_amount)
print(mustang.gas_amount, mustang.capacity)