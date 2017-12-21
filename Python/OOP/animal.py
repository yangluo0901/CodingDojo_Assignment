class Animal(object):
    def __init__(self, name, health):
        self.name =  name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Health of "+self.name+" is "+str(self.health)
a = Animal("Animal", 30)
a.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self,dog_name,dog_health):
        super(Dog,self).__init__(dog_name,dog_health)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,dragon_name, dragon_health):
        super(Dragon,self).__init__(dragon_name, dragon_health)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print "This is a dragon!"
        super(Dragon,self).display_health()

d = Dog("Biscuit",100)
d.walk().walk().walk().run().run().pet().display_health()

dr= Dragon("ekko",200)
dr.fly().fly().display_health()
