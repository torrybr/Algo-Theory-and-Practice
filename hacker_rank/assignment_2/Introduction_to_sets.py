def average(array):
    thisSet = set(array)
    sizeOf = sum(thisSet)
    return sizeOf / len(thisSet)


if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
