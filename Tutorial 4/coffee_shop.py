print("Welcome to the Python cappuccino Shop!")
 
customer_name = input("What is your name? ")
print("Hello, " + customer_name + "! Let's order some cappuccino.")
 
price_cappuccino = 4.50
price_latte = 5.00
price_mocha = 6.00
 
print("cappuccino: $" + str(price_cappuccino))
print("Latte: $" + str(price_latte))
print("mocha: $" + str(price_mocha))
 
choice = input("What would you like to order? (cappuccino/latte/mocha): ")
 
if choice == "cappuccino":
     cost = price_cappuccino
elif choice == "latte":
     cost = price_latte
elif choice == "mocha":
    cost = price_mocha
else:
     print("Sorry, we do not have that.")
     cost = 0
 
quantity = int(input("How many cups would you like? "))
 
total_cost = cost * quantity
 
if quantity > 1:
     print("You get a discount of $1.00!")
     total_cost -= 1.00

studentship = input("Are you a student? (yes/no) ")
if studentship == "yes":
    print("You get a 10% student discount!")
    total_cost = total_cost*0.9
 
print("Your total is: $" + str(total_cost))
print("Thank you, " + customer_name + "! Please come again.")
