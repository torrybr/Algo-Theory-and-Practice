if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    if query_name in student_marks:
        count = 0
        for i in student_marks[query_name]:
            count += i
    print '{0:.2f}'.format(count / len(student_marks[query_name]))
