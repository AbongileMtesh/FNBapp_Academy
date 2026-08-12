kilometers = float(input("How many KM are you driving? "))

pp = float(input("Petrol price per litre: R"))

litres_needed = kilometers/10

cost = litres_needed * pp

print(f"Final cost: R{round(cost,2)}")

