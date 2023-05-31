names = []
    
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")

#or we can make it more compact:
#with open("names.txt", "r") as file:
#    for line in sorted(file):
#        print("hello,", line.rstrip())

#or we can use lines = file.readlines() read all the line in the file

