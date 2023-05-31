def meow(n: int): #this is a typehint
    for _ in range(n):
        print("meow")

number: int = int(input("Number: ")) # there will be mypy error if this line is not converted to int
meows: str = meow(number)
print(meows)
#run: mypy meows_typehint.py
#to see the bug specifically for incompatible type in our code