arrayNums = [20, 10, 30, 2, 55, 28, 77]

for i in range(0, len(arrayNums)):
    for j in range(0, len(arrayNums)):
        if(j < (len(arrayNums) - 1)):
            if(arrayNums[j] > arrayNums[j + 1]):
                checkpoint = arrayNums[j]
                arrayNums[j] = arrayNums[j + 1]
                arrayNums[j + 1] = checkpoint
print(arrayNums)     