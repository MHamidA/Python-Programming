def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
    
def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            #pass #if you want to silently prompt the user
            print("x is not an integer")
        else:
            return x #break #but return is stronger than break even though it will be correct, but return in the other hadn not only return the value but also break the loops

main()