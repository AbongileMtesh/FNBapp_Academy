#Adding 2 numbers

num1 = input("Enter a number: ")
num2 = input("Enter a number: ")

print(num1+num2)
print(int(num1+num2))
print(int(num1)+int(num2))
#"hello" + "world" = helloworld
#data types
#string: hello, " 56#%$df7)"
#int: Integere whole numbers
#float: decimal numbers
#bool: true or false

#Type casting
#Calculate Tip
bill = float(input("What is the amount of th bill: R"))
tip = 0.15

value_tip = bill * tip
total_cost = bill + value_tip

print(f"The tip is: R{value_tip}")
print(f"The total cost is: R{total_cost}")