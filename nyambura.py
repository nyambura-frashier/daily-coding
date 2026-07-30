order=input("what's on your mind? ")
def cost(order):
   if order=="chapati":
      price="ksh 20"
   elif order=="kuku":
      price="ksh 8"
   return f"your total is {price}"
print(cost(order))
distance=input("how many miles to your home? ")
def cost(transportation):
   if distance <= "5 miles":
      price="KSH 50"
   else:
      price="ksh 50"+("ksh 10" *"distance")
print(cost(distance))
total=("(cost(order))"+"(cost(distance))")
print(total)
    



