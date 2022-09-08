# >>> string = "hello"
# >>> dir("hello")
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


string = "hello world! Hi!!"

# print(string.upper())
# #HELLO WORLD

# print(string.casefold())
# # hello world! hi!!

print(string.center(20))
#  hello world! Hi!!  

print(string.count("hello"))
#1

print(string.encode())
# b'hello world! Hi!!'

print(string.endswith("!!"))
#True

print(string.expandtabs())
#hello world! Hi!!

print(string.find("Hi!"))
# 13

txt= "hello {price:.2f}"
print(string.format(price=49))
# hello 49.00

a = {'x': 'Kousalya', 'y':'wendy'}
print("{x}'s last name is {y}".format_map(a))
# Kousalya's last name is wendy

print(string.index("world"))
#6

print(string.isalnum())
#False

print(string.isalpha())
#False

print(string.isascii())
#True

print(string.isdecimal())
#False

print(string.isdigit())
#False

print(string.isidentifier())
#False

print(string.islower())
#False

print(string.isnumeric())
#False

print(string.isprintable())
#True

print(string.isspace())
#False

print(string.istitle())
#False

print(string.isupper())
#False

print(" ".join(string))
# h e l l o   w o r l d !   H i ! !

a= "banana"
print(a.ljust(10))
# banana

print(string.lower())
# hello world! hi!!

print(string.lstrip(" world"))
# hello world! Hi!!

txt = string.maketrans("H", "S")
print(string.translate(txt))
# hello world! Si!!

print(string.partition("world"))
# ('hello ', 'world', '! Hi!!')

print(string.replace("hello", "kousalya"))
# kousalya world! Hi!!

print(string.rfind("hello"))
# 0

print(string.rindex("Hi"))
# 13

l = 8
print(string.rjust(10))
# hello world! Hi!!

print(string.rpartition("Hi"))
# ('hello world! ', 'Hi', '!!')

print(string.rsplit())
# ['hello', 'world!', 'Hi!!']

print(string.rstrip())
# hello world! Hi!!

print(string.split(" "))
# ['hello', 'world!', 'Hi!!']

print(string.splitlines())
# ['hello world! Hi!!']

print(string.startswith("H"))
# False

print(string.strip())
# hello world! Hi!!

print(string.swapcase())
# HELLO WORLD! hI!!

print(string.title())
# Hello World! Hi!!

print(string.upper())
# HELLO WORLD! HI!!

print(string.zfill(10))
# hello world! Hi!!




