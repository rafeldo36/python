# print("Hello World")
# print(5)

# import pandas
# # Read and work with a file named 'sample.csv'
# df = pandas.read_csv('sample.csv')
# print(df) # This will display first few rows from the words.csv file

# import hashlib  # This is an example of built in module
# m = hashlib.sha256()

# # Dont worry about how to use these modules just yet!

# print("Hello World", 7)
# print(5)
# print("Bye")
# print(17*13)

#This is a 'Single-Line Comment'
# print("This is a print statement.")

# """This is an if-else statement.
# It will execute a block of code if a specified condition is true.
# If the condition is false then it will execute another block of code."""
# p = 7
# if (p > 5):
#     print("p is greater than 5.")
# else:
#     print("p is not greater than 5.")
# escape sequence characters
# print("This will \" execute",13,sep="@", end="bye")

# a = complex(8, 2)
# b = True
# c = "Harry"
# d = None
# print(a)
# print(b)
# a1 = 9
# print(a + a1)
# print("The type of a is ", type(a))
# print("The type of b is ", type(b))
# print("The type of c is ", type(c))


# list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
# print(list1)

# tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
# print(tuple1)

# dict1 = {"name":"Sakshi", "age":20, "canVote":True}
# print(dict1)
    
# n = 15
# m = 7
# ans1 = n+m
# print("Addition of",n,"and",m,"is", ans1)
# ans2 = n-m
# print("Subtraction of",n,"and",m,"is", ans2)
# ans3 = n*m
# print("Multiplication of",n,"and",m,"is", ans3)
# ans4 = n/m
# print("Division of",n,"and",m,"is", ans4)
# ans5 = n%m
# print("Modulus of",n,"and",m,"is", ans5)
# ans6 = n//m
# print("Floor Division of",n,"and",m,"is", ans6)

# a = "1"
# # a = 1
# b = "2"
# # b = 2
# print(int(a) + int(b))

# # Implicit TypeCasting
# c = 1.9
# d = 8

# print(c + d)

# a = input("Enter your name: ")
# print("My name is", a)

# x = input("Enter first number: ")
# y = input("Enter second number: ")
# print(x  + y)

# print(int(x) + int(y))

# name = "Harry"
# friend = "Rohan"
# anotherFriend = 'Lovish'
# apple = '''He said, 
# Hi Harry
# hey I am good
# "I want to eat an apple'''
 
# print("Hello, " + name)
# # print(apple) 
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# # print(name[5]) # Throws an error
# print("Lets use a for loop\n")
# for character in apple:
#     print(character)

# fruit = "Mango"
# len1 = len(fruit)
# print("Mango is a", len1, "letter word.")

# pie = "ApplePie"
# print(pie[:5])
# print(pie[6])	#returns character at specified index

# pie = "ApplePie"
# print(pie[:5])      #Slicing from Start
# print(pie[5:])      #Slicing till End
# print(pie[2:6])     #Slicing in between
# print(pie[-8:])     #Slicing using negative index

# alphabets = "ABCDE"
# for i in alphabets:
#     print(i)

# str1 = "AbcDEfghIJ"
# print(str1.upper())

# str1 = "AbcDEfghIJ"
# print(str1.lower())

# str2 = " Silver Spoon "
# print(str2.strip())

# str3 = "Hello !!!"
# print(str3.rstrip("!"))

# str2 = "Silver Spoon"
# print(str2.replace("Sp", "M"))

# str2 = "Silver Spoon"
# print(str2.split(" "))      #Splits the string at the whitespace " ".

# str1 = "hello"
# capStr1 = str1.capitalize()
# print(capStr1)
# str2 = "hello WorlD"
# capStr2 = str2.capitalize()
# print(capStr2)

# str1 = "Welcome to the Console!!!"
# print(str1.center(50))

# str1 = "Welcome to the Console!!!"
# print(str1.center(50, "."))

# str2 = "Abracadabra"
# countStr = str2.count("a")
# print(countStr)

# str1 = "Welcome to the Console !!!"
# print(str1.endswith("!!!"))

# str1 = "Welcome to the Console !!!"
# print(str1.endswith("to", 4, 10))

# str1 = "He's name is Dan. He is an honest man."
# print(str1.find("is"))

# str1 = "He's name is Dan. He is an honest man."
# print(str1.find("Rafey"))

# str1 = "He's name is Dan. Dan is an honest man."
# print(str1.index("Dan"))

# # str1 = "He's name is Dan. Dan is an honest man."
# # print(str1.index("Daniel"))

# str1 = "WelcomeToTheConsole"
# print(str1.isalnum())

# str1 = "hello world"
# print(str1.islower())

# str1 = "We wish you "
# print(str1.isprintable())

# str1 = "        "       #using Spacebar
# print(str1.isspace())
# str2 = "        "       #using Tab
# print(str2.isspace())

# str1 = "World Health Organization" 
# print(str1.istitle())

# str2 = "To kill a Mocking bird"
# print(str2.istitle())

# str1 = "WORLD HEALTH ORGANIZATION" 
# print(str1.isupper())

# str1 = "Python is a Interpreted Language" 
# print(str1.startswith("Python"))

# str1 = "Python is a Interpreted Language" 
# print(str1.swapcase())

# str1 = "He's name is Dan. Dan is an honest man."
# print(str1.title())

applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
    
#     num = 0
# if (num < 0):
#     print("Number is negative.")
# elif (num == 0):
#     print("Number is Zero.")
# else:
#     print("Number is positive.")
    
    num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")