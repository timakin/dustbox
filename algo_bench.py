# Compare two ways of Search

import time
import random

def Search(target, numList):
    for x in numList:
        if x == target:
            return True
    return False

def Search2(target, numList):
    bubble(numList)
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

def bubble(numList):
    for i in range(len(numList)):
        for j in range(i+1, len(numList)):
            if numList[i] > numList[j]:
                tmp = numList[i]
                numList[i] = numList[j]
                numList[j] = tmp

def main():
    N = 10000
    
    numList = [random.randint(1,1000) for i in range(N)]
    numList2 = [x for x in numList]
    
    target1 = 5
    target2 = N/2
    target3 = N-5

    print N
    print

    print "Linear Search"
    start = time.clock()
    Search(target1, numList)
    finish = time.clock()
    print finish - start

    start = time.clock()
    Search(target2, numList)
    finish = time.clock()
    print finish - start

    start = time.clock()
    Search(target3, numList)
    finish = time.clock()
    print finish - start

    print 
    print "Search2"
    start = time.clock()
    Search2(target1, numList2)
    finish = time.clock()
    print finish - start

    start = time.clock()
    Search2(target2, numList2)
    finish = time.clock()
    print finish - start

    start = time.clock()
    Search2(target3, numList2)
    finish = time.clock()
    print finish - start

if __name__ == "__main__":
    main()