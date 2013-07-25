def Search(target, numList):
    for x in numList:
        if x == target:
            return True
    return False

def Search2(target, numList):
    min_pos = 0
    max_pos = len(numList) - 1

    while min_pos <= max_pos:
        mid_pos = (min_pos + max_pos) / 2

        if target == numList[mid_pos]:
            return True
        elif target > numList[mid_pos]:
            min_pos = mid_pos + 1
        else: # target < numList[mind_pos]
            max_pos = mid_pos - 1
    return False


if __name__ == "__main__":
    import time

    numList = [x for x in range(100000)]

    start = time.clock()
    Search(100, numList)
    print time.clock() - start

    start = time.clock()
    Search2(100, numList)
    print time.clock() - start
    print 

    start = time.clock()
    Search(90000, numList)
    print time.clock() - start

    start = time.clock()
    Search2(9000, numList)
    print time.clock() - start