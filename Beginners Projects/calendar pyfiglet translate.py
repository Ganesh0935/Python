#Calender in python Month

# import calendar
# m = calendar.month(2024,3)
# print(m)


# # Yearly Calendar in python

# print("\n #-----------#\n")

# from calendar import calendar
# y = calendar(2024)
# print(y)


# pyfiglet in Python
# install pip pyfiglet
from pyfiglet import figlet_format
f = figlet_format("KALKI")

print(f)




#pip install deep_translator
from deep_translator import GoogleTranslator
    
t = GoogleTranslator(
        source = 'hi',
        target= "en"
    )
r = t.translate("mera naam")
r = t.translate("Kaiso ho mera dosth.!")
print(r)