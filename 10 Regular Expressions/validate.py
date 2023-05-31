email = input("What's your email? ").strip()

username, domain = email.split("@")
    
if (username) and domain.endswith(".edu"): #if username = at least have one character 
    print("Valid")
else:
    print("Invalid")