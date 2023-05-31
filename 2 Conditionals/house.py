name = input("What's your name? ")


# python 3.10 >> only
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gyffindor")
    case "Draco":
        print("Slytherin")
    case _: #Selain anyone that is already matched
        print("Who?")