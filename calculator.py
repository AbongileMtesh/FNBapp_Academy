num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

if num2 == 0:
 print("Error please try again!")

Addidtion = num1 + num2
multiplication =  num1 *num2
division = num1 / num2
subtraction = num1 - num2

# print(f"Addition of the number: {round(Addidtion,2)}")
# print(f"Multipication of the numbers: {round(multiplication,2)}")
# print(f"Division of the numbers:{round(division,2)}")
# print(f"subtraction of the numbers: {round(subtraction,2)}")

floor_division = num1 // num2
modulas = num1 % num2

# print(f"Floor Division of the numbers:{round(floor_division,2)}")
# print(f"Modulas of the numbers: {round(modulas,2)}")

print(f"{'Addidtion'} | {'Multiplication'} | {'Division'} | {'Subtraction'} | {'Floor_division'} | {'Modulas'} |")

print(f"{Addidtion} | {multiplication} | {division} | {subtraction} | {floor_division} | {modulas} |")



