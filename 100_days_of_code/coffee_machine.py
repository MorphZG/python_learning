class CoffeeMachine:
    '''represent coffee machine'''
    def __init__(self):
        '''machine resources'''
        self.milk = 100
        self.water = 100
        self.coffee = 100
    
    def spend_resources(self, num):
        self.milk -= num
        self.water -= num
        self.coffee -= num
        return

machine = CoffeeMachine()
machine.spend_resources(1)
print(machine.milk)
        