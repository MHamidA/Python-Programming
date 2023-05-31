class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self): #always 1 argument
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name: # same with name == ""
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        #the error in the init method can be moved here because the self.house = house in the init function is also called this getter method
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) #constructor call

if __name__ == "__main__":
    main()