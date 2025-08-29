import random
n = random.randint(1,100)
a = -1
guessess = 1

while (a != n):
    a = int(input(" guess the number: "))

    if(a>n):
        print("Enter the lower number")
        guessess+=1

    elif(a<n):
        print("Ente the higher number: ")
        guessess+=1
print(f"You guess the number {n} in {guessess} attempts")


