import re

name = input("What's your name? ").strip()

if mathces := re.search(r"^(.+), *(.+)$", name): #walrus = if only if
    name = mathces.group(2) + " " + mathces.group(1)

print(f"hello, {name}")