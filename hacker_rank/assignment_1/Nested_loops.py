lis = []
scores = []
names = []
for _ in range(int(raw_input())):
    arr = []
    name = raw_input()
    score = float(raw_input())
    arr.append(name)
    arr.append(score)
    lis.append(arr)
for x in lis:
    scores.append(x[1])

for x in lis:
    if sorted(list(set(scores)))[1] == x[1]:
        names.append(x[0])

    names.sort()
for x in names:
    print x