import sys

if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) >2:
    sys.exit("too many arguments")

print("hello, my name is", sys.argv[1])

#python name.py Hamid