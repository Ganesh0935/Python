name = "Michael Jackson"
print(name[::-1])

print(reversed(name))
naam = reversed(name)
print(naam)
print(''.join(reversed(name)))
print(' '.join(naam))


pet = "cat"
print(list(pet))
s = reversed(pet)
print(list(s))#doubt #y output is [] when parameter is naam
print(list(reversed(pet)))

print(list(reversed("ant")))

for i in list(reversed(name)):
    print(i,end='')

print("\n--------------\n")
## Removing character from the Ending of the string
string_a = " karnan "
print(string_a.strip(" "))

print(string_a.lstrip(" "))
print(string_a.rstrip(" "))


string_n = "Happy Ugadi to all"
print(string_n.replace("Ugadi",'Holi')) 

# print(pet)
# pet[0]='s'
# print(pet) ## from here String is immutable

var = string_n.replace("a","A")
print(var)
print(id(string_n)) # id is different
print(id(var)) # id is different

print("hello \tworld".expandtabs())


print("\n#--------#-----------#\n")

string_s = "Hello Everyone. Welcome to 10th Birthday Party 2023"
print(string_s.replace("10th","18th").replace("2023","2024"))


pet1=pet.islower()
print(pet1)
print(pet.isupper()) # if pet= cAt both will be false
print(pet.isspace())
print(''.isspace())
print(' '.isspace())

abc = 'sdfghj4567'
print(abc.isalnum())

## string_name.isalnum()  NOte: all 'is' Functions are returns bool

if " ".isspace():
    print("\n+++++\n")

print(abc.startswith("s"))
print("hfukzdkj".endswith('j'))

## to count the no of characters in string
count=0
abc = 'sdfghj4567'
for i in abc:
    count=count+1
print(count)

## inbuilt function
print(len(abc))


## DO as many as inbuilt functions as userdefined

## Here are some examples

movie = 'Bahubali'
for i in movie:
    print(i)

print("\n#...........#\n")

for i in range(len(movie)):
    print(movie[i])

print(range(len(movie))) #range(0,8)
for i in range(len(movie)):
    print(i,"=",movie[i])

for i in range(len(movie)-1,-1,-1):
    print(movie[i],end='')

print("\n........\n")

movie_1 = 'Pushpa'
ch = len(movie_1)-1
while ch >= 0 :
    print(movie_1[ch])
    ch=ch-1


print("\n#...........#\n")

movie_2 = 'TEMPER'
for i in range(len(movie_2)):
    print(movie_2[len(movie_2)-(i+1)])

print("\n#...........#\n")


input = "Chagallu"
vowels = "aeiouAEIOU"
count=0
for ch in input:
    if ch in vowels:
        print("{} is Vowel".format(ch))
        count = count+1
    else:
        print("{} is not Vowel".format(ch))
print("Total no.of Vowles are {}".format(count))
print("Total no.of Consonants are",len(input)-count)


print("\n#...........#\n")



input_1 = 'Aditya#369AD'
a=b=c=0
for i in input_1:
    if i.isalpha():
        print(f"{i} is alphabet")
        a=a+1
    elif i.isnumeric():
        print(f"{i} is digit")
        b=b+1
    else:
        print(f"{i} is special character")
        c=c+1
print("{},{},{} are no.of alpha,digit,special characters respecively".format(a,b,c))


print("\n#...........#\n")


## LISTS


fruits = [1,23,'guava','berry',"Apple"]
#fruits = "Pomegranate"
for i in fruits:
 #   if i.isalpha():
        print(i)

print(name.split(" "))
print(list(name.split(" ")))
#both are same returns only list
print(list(name.split('a')))

Book = "Ramayan by Valmiki Maharshi"
print(list(Book))
print(list(Book.split(' ')))