class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...

class Student(Wizard):  #student inherit all the characteristic from wizard
    def __init__(self, name, house):
        super().__init__(name) #accesing super/parent class
        self.house = house
    

    ...

class Professor(Wizard):    #student inherit all the characteristic from wizard
    def __init__(self, name, subject):
        super().__init__(name) #accesing super class
        self.subject = subject

    
    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
