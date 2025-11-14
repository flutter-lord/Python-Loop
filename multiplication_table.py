print("            Multiplication Table")
print("  |", end = '')

for i in range(1,21):
    print("  ",i, end = '')

print("")

print("-------------------------------------------")


for j in range(1,21):
    print(j, "|", end = '')
    for i in range(1,21):
        print(format(i * j, "4d"), end = '')

    print()