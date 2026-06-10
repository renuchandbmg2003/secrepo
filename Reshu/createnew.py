# odd and even

n=int(input("enter any No."))
if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")


print("-------------------------------------")
print("Swapping")
a=5
b=10
print("before swapping")
print(a)
print(b)
print("after swapping")
a=a+b
b=a-b
a=b-a
print(a)
print(b)
