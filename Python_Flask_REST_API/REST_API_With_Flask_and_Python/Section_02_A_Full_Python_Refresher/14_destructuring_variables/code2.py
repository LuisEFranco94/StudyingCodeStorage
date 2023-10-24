student_attendance = {"Rolf": 96, "Bob":80, "Anne":100}

print(list(student_attendance.items()))

# for t in student_attendance.items():
#     print(t)

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

