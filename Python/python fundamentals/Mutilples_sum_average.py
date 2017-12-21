#Mutltiples,PartI
# for count in range(1,1001):
#     if count%2 != 0:
#         print count
#PartII

# count=1
# sum =0
# while True:
#     sum = 5*count
#     count+=1
#     if sum >1000000:
#         break
#     print sum
#Sum List/average list
a = [1, 2, 5, 10, 255, 3]
num = 0;
sum=0
while num < len(a):
    sum += int(a[num])
    num += 1
print sum/len(a)
