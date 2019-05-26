import person, orders
# Validate our person 
z = person.Person()
for i in z.__dict__:
    print(i,z.__dict__[i])
zo = orders.Orders(z.PersonID)

