from cs50 import get_string
from sys import exit

person = {
    "David": "08098574643",
    "Jude": "08063466372",
    "Simon": "09047362788"
}

name = get_string("Name: ")

if name in person:
    print(f"Number {person[name]}")
    exit(0)

print("Name not found")
exit(1)