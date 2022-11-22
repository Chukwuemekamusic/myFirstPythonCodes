from sys import argv

if len(argv) == 2:
    print(f"hello {argv[1]}")

else:
    print(f"hello world")

for arg in argv[1:]:
    #1 starts from [1] and -1 removes the last size away
    print(arg)
