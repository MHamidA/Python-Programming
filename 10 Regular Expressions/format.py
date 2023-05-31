import re

name = input("What's your name? ").strip()
mathces = re.search(r"^(.+), *(.+)$", name)

if mathces:
    last, first = mathces.groups()
    #last = matches.group(1)
    #first = mathces.group(2)
    name = f"{first} {last}"

    #or we can instead do this
    #name = mathces.group(2) + " " + mathces.group(1)

print(f"hello, {name}")