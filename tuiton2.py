i, tuition = 1, 10000
while i < 10:
    tuition += tuition * (5 / 100)
    i += 1

print("Your tuition in", i,"years is", tuition)