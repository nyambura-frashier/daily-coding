#input output and type convo

#user input
name=input("Enter your name: ")
print("What's up" + name)

#strings
#f strings-easier to read, 
#NO need to convert data types manually
#can include operators

Age=input("when were you born? ")
print(2026-int(Age))
print(f'you are {2026-int(Age)} years old')

#f string
height=input("what's your height in meters?" )
print(f'you height is {height}')

#errors
age=int(input("when were you born?"))
print((age)+10)
print(f'your age is {((age)+10)}')

#changing the value from one data type to another

age=20
print(float(age))

#strings and indexing
county="Nairobi"
print(county[0])
print(county[1])
print(county[-1])
print(county[:4])
print(county[:-4])

Name="Frashier"
print(Name.upper())
print(Name.lower())
print(Name.replace("Frashier","Nyambura"))
print(Name.split())
print(Name.strip())

#join!~ joins a list into one string