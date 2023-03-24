#this uses dictionary while loops and if conditions
#setting variable

menu={'Meat Lovers':5.95,' Summer Hawaiian':4.95,' VegDelight':3.95,'Chicken Barbeque':6.95,'Popping Pepperoni':3.59}

name = ""

more = "s"

qty = int(0)

total = 0

 

print('Welcome to pizza haven')

print('please place order from the following menu')

with open ('pizzamenu.txt', 'r') as f:
    read_content = f.read()
    print(read_content)

##f = open('pizzamenu.txt' , 'r')

##print(f.read())

##f.close()

 

print('')
name = input("Enter your name : ")
while more != 'n':


    item = input('Enter item name : ')
    if item not in menu:
        print('this item is not in menu')
        item = input('Enter item Name : ')
    try:
        qty = int(input('Enter quantity required : '))

    except ValueError:
        print('please enter positive numbers only')
        qty = int(input('Enter quantity required : '))
    price = menu[item]
    linetotal=price*qty
    total = total+linetotal




 
