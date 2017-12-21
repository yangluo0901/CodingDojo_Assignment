class mathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, arg1,*arg2):
        if len(arg2)>0:
            self.result += arg1
            for element in arg2:
                self.result += element
        else:
             self.result = arg1 + 0
        
        return self
    def subtract(self, arg1,*arg2):
        if len(arg2) >0:
            self.result += arg1
            for element in arg2:
                self.result -= element
        else:
            self.result = arg1 - 0

        return self
    def show_result(self):
        print self.result

md = mathDojo()
md.add(2).add(2,5).subtract(3,2).show_result()
