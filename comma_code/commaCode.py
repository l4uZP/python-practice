def CreateStringList(array):
    list = ""
    arrayLen = len(array)
    for x in range(arrayLen):
        value = str(array[x])

        if x == arrayLen-1:
            list = list + value
        elif x == arrayLen-2:
            list = list + value + " and "
        else:
            list = list + value + ", "
        
    return list