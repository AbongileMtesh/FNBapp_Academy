# A whilw loop

count = 4

while count > 0:
    print(count)
    count = count - 1

print("Blast off!!!")

#foor loop
for r in range(1,4):
    print(f"This is rep no.{r}")

#loops and decision making
# a guessing game

secret_word = "python"

while True: 
 guess = input("Guess the programming language: ").lower()

 if guess == secret_word:
    print("You guessed correctly, YAY!!!")
    break
 else:
    print("Incorrect try again!")




