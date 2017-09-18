if __name__ == '__main__':
    N = int(raw_input())
    arr = []
    for i in range(0, N):
        splitInput = raw_input().split(" ")
        if splitInput[0] == 'insert':
            #
            # insert x at position i
            arr.insert(int(splitInput[1]), int(splitInput[2]))
        elif splitInput[0] == 'remove':
            arr.remove(int(splitInput[1]))
        elif splitInput[0] == 'append':
            arr.append(int(splitInput[1]))
        elif splitInput[0] == 'pop':
            arr.pop()
        elif splitInput[0] == 'sort':
            arr.sort()
        elif splitInput[0] == 'reverse':
            arr.reverse()
        else:
            print arr




