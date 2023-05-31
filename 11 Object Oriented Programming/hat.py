#classmethod

import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod    
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

#no need to assign the class to var
Hat.sort("Harry")
