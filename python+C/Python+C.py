# learning variables

"""
Commenting
"""

x = 5
y = 'Caleb'
price = 60.5
print(x + price)

# casting 1.integer 2.string 3.float
# outputing
x = 3
x = "3"
x = 3.0

print(x)
print(type(x))

# Case sensitivity

price = 20
Price = 40
PRICE = 60
pricE = 80
print(PRICE)

x, y, z = "orange", "cherry", "banana"
print(x)
print(y)
print(z)

x = y = z = "120"
print(x)
print(y)
print(z)

# operators
x = 5
x += 3  # this is like saying x=x+3
x = x + 3
x *= 4  # its like multiplying 11 by 4
print("my answer is:", x)

# means equal to each other
y = 9
y = 6
print(y == 6)

# means not equal to
p = 5
o = 7
print(p != o)

# CONDITIONAL STATEMENTS

age=5
# the if code executes when condition is set and is only true
if age>=18:
    print("You are an adult")

 # logical operator
    age = 40
    nationality = "kenyan"
    if nationality == "kenyan" and age > 35:
        print("You can be president")
    else:
        print("You cannot be president")

#the elif statement
if age > 18:
    print("Adult")
elif age<18:
    print("Child")

a=10
b=20
if a>b:
    print("a is greater than b")

elif a ==b:
    print("a nad b are equal")

else:
    print("a is less than b")

# checking if a number is even or odd
    number = 8

    if number % 2 == 0:
        print("even")
    else:
        print("odd")

#Casting
    first_name="Caleb "
    last_name="Kimutai"
    full_name=first_name+last_name
    print(full_name)

# Integer to String
    first_name = "Caleb "
    last_name =10
    full_name = first_name + str(last_name)
    print(full_name)

#String to float
    pens_total=50
    books_total="100"
    grand_total=int(books_total)+pens_total
    print(grand_total)

#String to float
    pens_total = 50.80
    books_total = "100"
    grand_total = float(books_total) + pens_total
    #concatitation of which is combining two strings together
    result=str(grand_total)+" Ksh"
    print(result)

    #Loooping in python
    # the while loop
    #break to stop before threee
    i=1
    while i<=10:
        if i == 3:
            break
        i+=1
        print(i)
        #increment after you do what you want to do

        while i <= 10:
            i+=1
            if i == 3:
                continue
            print(i)


allowed_country = "Kenyan"
allowed_count = 3
denied_count = 2

allowed = 0
denied = 0

while allowed < allowed_count or denied < denied_count:
    entry = input("Enter your country: ")
    if entry == allowed_country and allowed < allowed_count:
        print("you are Kenyan , You are allowed entry .")
        allowed += 1

    else:
        print("Sorry, you are a visitor. you are not", allowed_country)
        denied += 1

print("Total number of Kenyan's allowed:", allowed)
print("Total number of visitors denied:", denied)

#for loop in python
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)










