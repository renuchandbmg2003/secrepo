print("------------sum of Natural No.-------")
num=int(input("Enter a number here"))
if num<0:
    print("Please enter positive Number")
else:
    sum=0
    while num>0:
        sum +=num
        num -=1
    print("sum of natural No. is ")
    print(sum)


print("---------------OR---------------------")



sum=0
i=1
while i<10:
    sum=sum+i
    i=i+1#---------------i+=1------------
print(" Sum of first 10 natural No is ")
print(sum)