import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = "stranger"

print(f"Hello {name}!")
