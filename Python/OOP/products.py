# -*- coding: utf-8 -*-
class product(object):
    def __init__(self,price,name,weight,brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
    def addTax(self,tax):
        if isinstance(tax,float):
            self.price += self.price*tax
        return self
    def Return(self,reason):
        if reason.count("defective") >= 1:
            self.price = 0
            self.status = "defective"
        elif reason.find("box") != -1:
            self.status = "for sale"
        elif reason.count("opened") > 0 :
            self.status = "used"
            self.price = self.price*0.8
        return self
    def display_info(self):
        print self.name + "\nPrice:" + str(self.price)+"\nWeight: "+str(self.weight)+" lb"+"\nBrand:"+self.brand+"\nStatus:"+self.status


toy = product(100, "dog toy", 2, "Gucci")
toy.addTax(0.9).Return("i opened this gift but dont like it").display_info()
