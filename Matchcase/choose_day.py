# from unittest import case
#
# print("-------------enter day's No.------------------")
# day=int(input("enter the day"))
# match day:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5:
#         print("friday")
#     case 6:
#         print("saturday")
#     case 7:
#         print("sunday")
#     case _:
#         print("Invalid input")


# a=int(input("enter any no for A="))
# b=int(input("enter any no for B="))
# result=int(input("case 1 for add, 2 for sub, 3 for mul, 4 for div, 5 for mod, 6 for divi"))
# match result:
#     case 1:
#         print(a+b)
#     case 2:
#         print(a-b)
#     case 3:
#         print(a*b)
#     case 4:
#         print(a/b)
#     case 5:
#         print(a//b)
#     case 6:
#         print(a%b)
#     case _:
#         print("Invalid option")


print("--------------weekend day's---------------")
print("-------------------------------------------")
day=int(input("enter any no for day"))
match day:
    case 1|2|3|4|5:
        print("week day ")
    case 6|7:
        print("weekend day ")