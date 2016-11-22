
print("  Example 1  ")
print()
x = [400, 500, 100]
nx = enumerate(x)

for i, xi in nx:
    print(i, xi, x[i])
    x[i] += 10
print(x)