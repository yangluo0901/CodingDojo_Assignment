# Part I

def draw_star(list):
    str = ""
    for element in list:
        for num in range (element):
            str +="*"
        print str


#PartII


def draw_star1(list):

    for element in list:
        string = ""
        if isinstance(element, str):
            for count in range(len(element)):
                string += element[0]+" "
        elif isinstance(element,int):
            for count in range (element):
                string += "*"
        print string

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]


draw_star1(x)
