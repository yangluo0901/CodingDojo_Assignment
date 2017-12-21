class Car(object):
    def __init__(self,price, speed, fuel, mileage):
        self.price = price
        self.fuel = fuel
        self.speed = speed
        self.mileage = mileage
        self.tax = 0
        self.display_all()
    def cal_tax(self):
        if self.price >10000:
            tax = 0.15
        else:
            tax = 0.12
        return self
    def display_all(self):
        print "Price: "+str(self.price)+"\n" +"Fuel: "+str(self.fuel)+"\n"+"Speed: "+ str(self.speed) +" mph\n"+"Mileage: "+ str(self.mileage)+" mpg\n"+"Tax: "+str(self.tax)


car1 = Car(2000, 35, 'Full', 15)
car2 = Car(2000, 5, 'Not Full', 105)
car3 = Car(2000, 15, 'Kind of Full', 95)
car4 = Car(2000, 25, 'Full', 25)
car5 = Car(2000, 45, 'Empty', 25)
car6 = Car(20000000, 35, 'Empty', 15)
