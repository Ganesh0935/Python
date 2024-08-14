# a=10
# print("My First Program")
# print(a*a)

# name="DEV"
# age=18
# degree='MBBS'
# print(f"My name is {name} and my age is {age} with degree {degree}")
# print("MY name is ",age,name,degree)
# print("MY name is {} and I am {} with {} degree".format(name,age,degree))
# print("I have completed {a} at age {k} and Here I am {t} ".format(k=age,t=name,a=degree))

# num=int(input("Enter the age:"))
# #num=14
# if num < 10:
#     print("You are Kid ")
# elif num>=10 and num<=12 :
#     print("You are Matured Kid ")
# elif num >= 13 and num <= 19:
#     print("You are Teenager")
# else:
#     print("You are Aged")



q='Tanguturi prakaham pa38urweugfu'
x=12
print(x)
print(type(x))

print(type(True))

y="Son of INDIA"

print(f"Mohan Babu last film is {y}")

print("MOhan BAbu last filmm is ",y,q)

print("Mohan bau last film is {} and Once his son said {}".format(y,q))

print("Manchu Vishnu said {c} and HIS FATHER last film is {r}".format(r=y,c=q))


print("\n#------------------------#\n")


# is vs == OPERATORS
lst_a = [1,2,3,4]
lst_b = [1,2,3,4]
k=lst_a is lst_b #memory address is checking
print(k) #False
k=lst_a is not lst_b
print(k) #True

q = lst_a == lst_b # value are checking
print(q) #True