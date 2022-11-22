from cs50 import get_string

s = input("do you agree ")

if s.lower() in ["y", "yes"]:
    print("agreed")
elif s.lower() in ["n", "no"]:
    print("not agreed")

# another syntax
g = input("do you agree ").lower()

if g in ["y", "yes"]:
    print("agreed")
elif g() in ["n", "no"]:
    print("not agreed")