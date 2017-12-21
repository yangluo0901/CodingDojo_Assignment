#integer
def integer(obj):
    if isinstance(obj,int):
        if obj>=100:
            print "That is a big number!"
        else:
            print "That is a small number!"
    elif isinstance(obj,str):
        if len(obj)>=50:
            print "Long sentence"
        else:
            print "Short Sentence"
    elif isinstance(obj,dict):
        if len(obj)>=10:
            print "Big list"
        else:
            print "Short List!"



a = {"yangluo":"male","ranli":"female"}
integer(a)
print len(a)
