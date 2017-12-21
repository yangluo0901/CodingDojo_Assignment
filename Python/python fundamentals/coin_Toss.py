import random
def coin_Toss(command):
    if command == "start":
        print "Starting the program ... "
        h = 0
        t = 0
        for count in range(50000):
            num =  random.randint(0,1)
            if num == 0:
                str =  "head"
                h+=1
            else :
                str =  "tail"
                t+=1
            str = "Attempt #",count," : Throwing a coin... It's a " + str+" ... Got ",h,"head(s) so far and ",t," tail(s) so far"
            print str
        print "Ending the program, thank you !"


coin_Toss("start")
