import numpy

def arrays(arr):
    list(reversed(arr))
    b = numpy.array(arr[::-1],float)

    return b

if __name__ == '__main__':
    arr = raw_input().strip().split(' ')
    result = arrays(arr)
    print(result)