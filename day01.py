print("Hello world")
print("My name is the menace")

# comment

input

#~python data types~
#123- integers
#Nairobi- string
#3.12-float
#True-boolean

#Boolean
its_raining=True
its_hot=False

print(its_raining)
print(its_hot)

#variables are not enclosed by speech marks

age=18
print("My name is the menace and i am",age,"years old")
print(f'My name is the menace and i am {age}')

#f string is a formated string that allows you to insert variables directly using a
#curly bracket

print("My name is the menace" + str(18) + "years old")

#type functions
year=2020
university="Jomo kenyatta university of agriculture and technology"

print(type(year))
print(type(university))

#Global variables- you can change your dat type
x="Nairobi"

def myfunc():
    global x
    x="Mombasa"
myfunc()
print("I live in", x)


