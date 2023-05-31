#with open("students.csv") as file:
#    for line in file:
#        name, house = line.strip().split(",")
#        print(f"{name} is in {house}")

import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file) #we can use csv.reader too but it is more much better to use DicReader if the csv have header
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

#note
#key=lambda student: student["name"]
#equal to
#def get_name(student):
#    return student["name"]   
##I use lambda since the get_name function is only used once