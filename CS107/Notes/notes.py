print("  Example 1 ")
print()
colors = ["red", "yellow", "green"]
if "red" in colors:
    print("Red is in colors")
else:
    print("Red is not in colors")

print()
print("  Example 2  ")
print()
listA = ['a', 'b', 'c', 'd', 'e', 'f']
num_letters = len(listA)
midpoint = num_letters / 2
fist_letters = listA[:midpoint]
last_letters = listA[midpoint:]
