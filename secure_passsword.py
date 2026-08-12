passwword = input("Enter your password: ").strip()

VF = f"{passwword[0]}"
VL = f"{passwword[-1]}"

print(f"Your password hint: it starts with {VF} and ends with {VL}")