print(True and False) # False
print(True or False)  # True

print(bool(1)) #True

print(int(bool(0))) # 0

print(not 0) # True



START=1
STOP=0
print(f"Value of Start ny negativing stop is {int(not STOP)}")  # Value of Start ny negativing stop is 1
 # not STOP is True and then it is typecasted

print(not STOP) # True
print(f"Value of Stop by negativing Start is {(int(not START))}") # Value of Stop by negativing Start is 0



print("\n #........1.........# \n")






zero = 0
one = 1
print(f"Negation of {zero} is {not zero}") # Negation of 0 is True
print(f"Negation of {one} is {not one}") # Negation of 1 is False

print(f"bool value of {zero} is {bool(zero)}") # bool value of 0 is False
print(f"Bool value of {one} is {bool(one)}") # Bool value of 1 is True


print("\n #...........2........#\n")





some_negative=-3
some_positive=3
print(f"Boolean value of {some_negative} is {bool(some_negative)}")# Boolean value of -3 is True
print(f"Boolean value of {some_positive} is {bool(some_positive)}")# Boolean value of 3 is True
print(f"negation of {some_positive},{some_negative} is always {(not some_negative) and (not some_positive)}")
# negation of 3,-3 is always False




print("\n#.......3.......#\n")




print(False * (not(True))) # 0
print(not (False)* False) # True
print(not True) # False
print(False * (not(True))) # 0
#print(False * not(True) )  returns syntax error
print(True and not False) # True
print(not False * False) # True
## () * not and or implies biimplies
## not and or implies biimplies note:(and,or) precedency is left to right
#AUTo is right to left


## Functions
def Hello_World(str):
 print(str)

Hello_World("print") # print


str1='Prabhas'
str2='Prabhas'
#id is identity like address
print(id(str1)) # 2179020380304
print(id(str2)) # 2179020380304




print("\n------------4--------------\n")



print(dir(str1)) #displays all in built functions of string
""" ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', 
 '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__',
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']  """


print("\n\n---#----------5----------#----\n\n")



var=10
print(bin(var)) # 0b1010

Disorder = 'Imagino Romanco Filia'
# Disorder="GANESH"
# print(Disorder[3])
# print(Disorder[-5:-4])
print(Disorder[:]) # Imagino Romanco Filia



print("\n -------6----------\n")



name = "Karthik"
print(name[-5:4])
print(Disorder[:-12])#from first to -12 postion
print(Disorder[-12:])#-12 to last position

print(Disorder[-12:15])
print(name[::-1])#Reverses the string
print(name[::-2])# Reverse the string with twosteps ahead from last pos
print(name[::-3])

print(name[2::3])#2 is first position and prints then initialize it with 0 and here 3 is next position 
print(name[::2])
print(name[4::-2])#upto 4th position and then reverse it

print(name[3:1:-1])


course_name="Data Science Masters"
print(course_name[5:12])#[5:12:1]
print(course_name[11:4:-1])


#concatenation
print(course_name + " ImaginoRomancofilia")
print(course_name*3)
print((course_name + " ")*3)

#len(strname) function
print(len(course_name))

#find function
print(course_name.find("m"))#lowest index in string
print(course_name.find("a",2,10)) #index range


#count function
print(course_name.count(''))#empty # value should be given even it is empty
print(course_name.count(' '))#spaces
print(course_name.count('Science'))

#split and Partion fns
n=course_name.split('S')
print(n)
print(course_name.partition('S'))

#cases functions
print(course_name.lower()) #lowercase
print(course_name.upper()) #uppercase
print(course_name.title()) #first letter of word is Captilized
print(course_name.swapcase()) # case is inversed



#method method combined

print(course_name.lower().count('s'))

print(course_name.upper().count('s'))

print(course_name)
hi=course_name.split(" ")
print(hi)
line="-".join(hi)
print(line)


def mutate_string(string, position, character):
   string = string[:position]+ character + string[position+1:]
   return string
    # l=list(string)
    # l[position]=character
    # string=''.join(l)
    # return string


s_new = mutate_string("Animal",3,"N")
print(s_new)


print(name[::])

var = 10
print(bin(var))
print(~var)

print("\n ----------7----------\n")


# OUTPUT FOR ABOVE CODE(6 to 7)
'''
 -------6----------

rt
Imagino R
omanco Filia
omanco
kihtraK
khrK
ktK
ri
Krhk
hrK
tr
Science
ecneicS
Data Science Masters ImaginoRomancofilia
Data Science MastersData Science MastersData Science Masters
Data Science Masters Data Science Masters Data Science Masters 
20
-1
3
21
2
1
['Data ', 'cience Masters']
('Data ', 'S', 'cience Masters')
data science masters
DATA SCIENCE MASTERS
Data Science Masters
dATA sCIENCE mASTERS
3
0
Data Science Masters
['Data', 'Science', 'Masters']
Data-Science-Masters
AniNal
Karthik
0b1010
-11

 ----------7----------
'''