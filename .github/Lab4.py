# Programmers: Callie Walker, Lesdy Galvez, Hanna Magan
# Course Name: CS151 Dr. Rajeev
# Date: 10/7/21
# Lab Number: 4
# Program Inputs: The type of package, if the green package uses a coupon
# Program Outputs: How much the customer owes

subscription = input("Enter the type of subscription: ")
subscription = subscription.strip().lower()
cost = 0
#This section of if statements separately creates variavkes to calculate the cost of the subscriptions.
if(subscription == "green"):
    extraCost = 14.99
    planGigs = 2
elif(subscription == "orange"):
    extraCost = 9.99
    planGigs = 4
#This set of conditionals evaluates which subscription the user inputted and calls on previous defined variables to calculate the cost.
if subscription == "green":
    cost += 49.99
    gigs = int(input("Enter the amount of gigs used this month "))
    if (gigs > planGigs):
        cost += (gigs - planGigs) * extraCost
        if(cost >= 75):
            discount = input("Enter 'yes' or 'no' if you have and would like to use a coupon ")
            discount_str = discount.strip().lower()
            if(discount_str == "yes"):
                cost -= 20
    print("You owe $", cost)
elif(subscription == "orange"):
    cost = 69.99
    gigs = int(input("Enter the amount of gigs used this month "))
    if(gigs > planGigs):
        cost += (gigs - planGigs) * extraCost
    print("You owe $", cost)
elif (subscription == "purple"):
    cost = 99.99
    print("You owe $", cost)
else:
    print("invalid subscription name")




