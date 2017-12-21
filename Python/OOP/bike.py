#Assignments for OOP-Bike, 12/04/2017
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print self.price, self.max_speed,self.miles

    def ride(self):
        self.miles += 10
        return self
    def reverse(self):
        if self.miles >=5:
            self.miles -= 5
            return self

# create three instances

bike_1 = Bike(1000,40)
bike_1.reverse().displayinfo()


bike_2 = Bike(1500,50)
bike_2.ride().ride().reverse().reverse().displayinfo()

bike_3 = Bike(2000, 60)
bike_3.reverse().reverse().reverse().displayinfo()
