class Student:
    def __init__(self, name, house, patronus):
        if not name: # same with name == ""
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self): #always 1 argument
        return f"{self.name} from {self.house}"

    def charm(self):
        if self.patronus == "Stag":
            return "🦌"
        elif self.patronus == "Otter":
            return "🦦"
        elif self.patronus == "Jack Russell terrier":
            return "🐶"
        else:
            return "🪄"    
        #match self.patronus: #match method is only available for python 3.10>
        #    case "Stag":
        #        return "🦌"
        #    case "Otter":
        #        return "🦦"
        #    case "Jack Russell terrier":
        #        return "🐶"
        #    case _:
        #        return "🪄"

def main():
    student = get_student()
    #print(student)
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus) #constructor call

if __name__ == "__main__":
    main()