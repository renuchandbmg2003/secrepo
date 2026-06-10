########################------Arithmetic operator----#####################
print("______________Arithmetic operator_____________________")
a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)## if contain float value
print(a%b)
print(a//b) ## it contain int value



#######################--------Relational operator-----------#######################
print("________Relational operator___________________")
a=10
b=20
if a>b:
    print("a is greater than b")
else:
   print("b is greater than a")

print("---------------------------------")
print("The value of a",a)
print("The value of b",b)
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(b>a)
print(b==a)


###########################--------Arithmetic----##############################
print("--------Arithametic operator------")
a=10
b=3
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>b)



###########################------exponent------##########################
print("___________exponent_________________")
a=10
b=3
print(a**b) ## 10 ka cude##




############################-----logical operator-------########################
print("_________logical operator__________________")
age=21
b=1000
print(age>20 and b>500)
print(age>18 or b>200)
print(~(age>b))####???????????????----  -1 kyu hai iska Answer




#############################-----Membership------######################################
print("_______membership_________________")
mylist=[1,2,3,4,5]
print(1 in mylist)
print(20 not in mylist)




#############################----identity operator---###############################
print("------identify operator--------")
a=[1,2,3,4,5,6]
b=a
print(a is b)
print(b is not a)




#########################---marks obtain------###########################
print("________Marks obtain___________________")
eng=59
print("english marks = ",eng)
hin=90
print("hindi marks =",hin)
math=65
print("math marks =",math)
sci=20
print("science marks =",sci)
sst=78
print("sst marks =",sst)

tot=eng+hin+math+sci+sst
print("total marks obtain",tot)

per=tot*5/100
print("percentage obtain",per)




#########################-----odd & Even------#############################
print("---------No. is even or odd---------------------")
No=2
if No%2==0:
    print("No is even")
else:
    print("No is odd")





print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("enter any No.")
if No%2==0:
    print("No is even")
else:
    print("No is odd")






#######################-------Unary operator__________##############
print("------Unary operator_____")
print("pree & post increment")
a=50
b=35
print("The value of a is =",a)
print("The value of b is=",b)
print("after increment")
x=++a
print("The value of x is=",x)
y=b+1
print("The value of y is=",y)


#--------------------------------------------------------------------------#


print(---------"pree & post decrement---------")
a=9
b=11
print("The value of a is =",a)
print("The value of b is=",b)
x=--a
print("after decrement")
print("The value of x is=",x)
y=b-1
print("The value of y is=",y)




####----------------- No. is positive or negative---------------------#############
print("________No. is positive or negative_______________")
print(" Enter any No.")
if a>0:
    print("No. is positive")
else:
    print("No. is negative")