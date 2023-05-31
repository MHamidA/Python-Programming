import re

url = input("URL: ").strip()

#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
#print(f"Username: {username}")

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE): # use the ?: so it will not be returned
    print(f"Username: {matches.group(1)}")