if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    m = int(raw_input())
    arr2 = map(int, raw_input().split())
    arr2 = set(arr2)
    arr = set(arr)

    arr3 = arr.difference(arr2)
    arr4 = arr2.difference(arr)

    finallis = list(arr3) + list(arr4)

    finallis.sort()
    for i in finallis:
        print i
