import csv
import random
filename = "Menu.csv"


def pattern1():

    print("****\t\t****")
    print("|  |\t\t|  |")
    print("|  |\t\t|  |")
    print("|  |\t\t|  |")
    print("****\t\t****")
    print("\n")
    print("       {}       ")
    print("      ____      ")


def pattern2():

    print(" **** ")
    print("*    *")
    print("*    *")
    print("*    *")
    print("*    *")
    print(" **** ")

 
file = open(filename)
csvreader = csv.reader(file)
index = []
index = next(csvreader)
print(index[0] + "\t    " + index[1] + "\t    " + index[2])
entry = []
for row in csvreader:
    entry.append(row)
file.close()   



for row in entry:
    for col in row:
        print(col,end=" ")
        print("\t\t",end=" ")
    print()    

customerorder = []
while(1):
    print("Would you like to order something. enter Y/N")
    i = input()
    if i.upper() == "Y":
        order = []
        print("Tell the Item no you would like to order")
        id = int(input())
        order.append(id)
        print("half/full:")
        plate = input()
        order.append(plate)
        print("Enter quantity you like to order:")
        quant = int(input())
        order.append(quant)
        customerorder.append(order)
    elif i.upper() == "N":
        break

    else:
        print("Wrong key is pressed")   


print("\nYOUR ORDERED ITEM ARE:")
print(index[0] + "\t    " + index[1] + "\t    " + index[2])
for row in customerorder:
    for col in row:
        print(col,end=" ")
        print("\t\t",end=" ")
    print()

tipped = [0,10,20]
print("Select how much tip you want to add from the below:")
for i in tipped:
    print(i,"%")
    

print("\nPress any of 1,2,3 from above to add that much tip in percentage:")
choice = int(input())
if choice == 1:
    tip = 0
elif choice == 2:
    tip = 0.1
elif choice ==3:
    tip = 0.2

print(tip)

total = 0
for row in customerorder:
    for value in entry:
        if row[0] == int(value[0]):
            if row[1] == "full":
                total = total + row[2] * int(value[2])
            else:
                total = total + row[2] * int(value[1])

tipped_amount = total*tip
total_bill = total + total * tip
#print(total)
print("Your total bill of food including tip is:")
print(format(round(total_bill,2), '.2f'))
print("The bill will be splitted in how many people?")
split = int(input())
bill_perperson = total_bill / split

print("The bill per person is:")
print(format(round(bill_perperson,2), '.2f'))
print("The restaurant has a limited time event called 'Test your luck'")
print("Would you like to participate Enter Y/N")
decision = input()
if(decision.lower() == "y"):
    print("okay Time to see how lucky you are")
    x = random.randint(1,100)
    if x in range(1,6):
        print("Congratulations! you have won 50% discount on your bill")
        discount = 0.50
        discounted_price = discount * total_bill
        print("Discount in value is:",end=" ")
        print(format(round(discounted_price,2), '.2f'))
        print("\n")
        pattern1()
    elif x in range(6,16):
        print("Congratulations! you have won 25% discount on your bill")
        discount = 0.25
        discounted_price = discount * total_bill
        print("Discount in value is:",end=" ")
        print(format(round(discounted_price,2), '.2f'))
        print("\n")
        pattern1()
    elif x in range(16,31):
        print("Congratulations! you have won 10% discount on your bill")
        discount = 0.10
        discounted_price = discount * total_bill
        print("Discount in value is:",end=" ")
        print(format(round(discounted_price,2), '.2f'))
        print("\n")
        pattern1()
    elif x in range(31,51):
        print("Oh! you have not got any discount on your bill")
        discount = 0.00
        discounted_price = 0.00
        print("Discount in value is:",end=" ")
        print(format(round(discounted_price,2), '.2f'))
        print("\n")
        pattern2()
    else:
        print("Unlucky day for you, you got increase in bill")
        discount = 0.20
        discounted_price = discount * total_bill
        print("Increase in value is:",end=" ")
        print(format(round(discounted_price,2), '.2f'))
        print("\n")
        pattern2()

print("\n")
print("The total breakdown of your bill is:")
print("Tip Percentage:",format(round(tipped_amount,2), '.2f'))
if discount == 0.20:
    print(f"Discount/Increase: +{round(discounted_price,2):.2f}")
    complete_bill = total_bill + discounted_price
elif discount == 0.00:
    print("Discount/Increase: 0.00")
    complete_bill = total_bill
else:
    print(f"Discount/Increase: -{round(discounted_price,2):.2f}")
    complete_bill = total_bill - discounted_price







