def take_students(num):
    l = []
    for i in range(num):
        student = input()
        if student == "Daniyar":
            return 'teacher can not be student'
        l.append(student)

    return l

print(take_students(3))
