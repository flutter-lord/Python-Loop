for i in range(1, 4):
    for j in range(1, 4):
        if i * j > 2:
            continue
        print(i * j)

    print(i)