print("Q1.find Armstrong No.")
num=int(input("Enter a number here"))
temp=num
sum=0

while num>0:
    r=num%10
    sum=sum+r*r*r
    num=num//10
    if temp==sum:
        print("The No. is armstrong")
    else:
        print("The No. is not armstrong")

