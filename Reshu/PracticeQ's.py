#                   QUESTION
# Python program to display the multiplication table.
# Python program to find Armstrong number in an interval.
# Python program to find the sum of natural numbers.
# Python program to find HCF.
# Python program to convert decimal to binary, octal and hexadecimal.
# Python program to find factorial of a number.

print("Q1.find Armstrong No.")
print("-------------------------------")
print("solution")
n=int(input("Enter any No."))
temp=n
s=0

while n>0:
    r=n%10
    s=s+r*r*r
    n=n//10

    if temp==s:
        print("No. is Armstrong")
    else:
        print("No. is not Armstrong")


