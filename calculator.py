from cs50 import get_int
import sys

x = get_int("x: ")
y = get_int("y: ")
print(f"the sum is equal to {x + y}")

try:
    s = int(input("s: "))
except:
    print("error datatype")
    sys.exit()
try:
    p = int(input("p: "))
except ValueError:
    print("error datatype")

print(f"the sum of s and p is {s + p}")

