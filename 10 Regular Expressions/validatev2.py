import re

email = input("What's your email? ").strip()

if re.search(r"^(\w|\.)+@(\w|\.)+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

#official regex for email in browser nowadays (simplified):
# ^[a-zA-Z0-9.!#$%&'*+\/=?^_'{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$