
import requests
import pyfiglet
import sys
import time
import json

# Terminal color codes
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
Ab = '\033[1;92m'
aB = '\033[1;91m'
AB = '\033[1;96m'
aBbs = '\033[1;93m'
AbBs = '\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'

# Generate large ASCII art for the title
title_art = pyfiglet.figlet_format("IFSC OSINT")
print(f"{Ab}{title_art}")

# Print the emoji separately for additional flair
print(f"{G}🔍Only for ethical purpose{aB}")

def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)

to(f"Welcome to the IFSC Code Osint")

# Get the IFSC code from the user
ifsc_code = input('Enter IFSC Code==>  ')
print("\n")

# Request data from Razorpay's API
u = f'https://ifsc.razorpay.com/{ifsc_code}'
response = requests.get(u)

# Check if the request was successful
if response.status_code == 200:
    # Load the response as JSON
    data = json.loads(response.text)
    
    # Display the formatted data with colors
    print(f"{Ab}BANK: {G}{data['BANK']}")
    print(f"{Ab}IFSC: {G}{data['IFSC']}")
    print(f"{Ab}BRANCH: {G}{data['BRANCH']}")
    print(f"{Ab}ADDRESS: {G}{data['ADDRESS']}")
    print(f"{Ab}CONTACT: {G}{data['CONTACT']}")
    print(f"{Ab}CITY: {G}{data['CITY']}")
    print(f"{Ab}RTGS: {G}{data['RTGS']}")
    print(f"{Ab}DISTRICT: {G}{data['DISTRICT']}")
    print(f"{Ab}STATE: {G}{data['STATE']}")
else:
    print(f"{E}Failed to retrieve data. Status code: {response.status_code}")

