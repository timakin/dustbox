def pow1(x, n):
    if n == 0: return 1
    value = pow1(x, n / 2)
    value *= value
    if n % 2 == 1: value *= x
    return value

if __name__ == "__main__":
    import time

    start = time.clock()
    pow1(5,10)
    finish = time.clock()
    time = finish-start
    print time
   

    start = time.clock()
    pow1(5,1000)
    finish = time.clock()
    time = finish-start
    print time
   