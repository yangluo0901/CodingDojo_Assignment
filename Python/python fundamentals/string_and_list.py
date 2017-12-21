words="It's thanksgiving day. It's m birthday too!"
print words.find("day");
words1 = words.replace("day","month",1)
print words1
x = ["hello",2,54,-2,7,12,98,"world"]
print max(x)
print min(x)
print x[0]
print x[len(x)-1]
x1 = [19,2,54,-2,7,12,98,32,10,-3,6]
new_x1=sorted(x1);print new_x1
# print new_x1.split(",");
first_half = new_x1[:5]; print first_half
second_half = new_x1[5:]; print second_half
second_half.insert(0,first_half)
print second_half
