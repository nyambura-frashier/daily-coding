order=input("order up:" )
def cost(order):
    if order == "bicycle" :
        price ="$5"
    elif order == "toycar":
        price ="$12"
    elif order =="tyres":
        price ="$18"
    else:
        price="$25"
    return f"your cost is{price}"
print(cost(order))


