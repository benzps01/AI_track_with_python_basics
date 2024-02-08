names = input("Enter name with comma: ").split(",")
assignments = input("Enter assignments counts: ").split(",")
grades = input("Enter grade count: ").split(",")

message = "Hi {}\n\nThis is a reminder that you have {} assignments left to submit before you can graduate. Your current grade is {} and can increase to {} if you submit all assignments before the due date.\n\n"

for i in range(len(names)):
    name = names[i]
    assignment = assignments[i]
    grade = grades[i]

    print(
        message.format(
            name, assignment, int(grade), (int(grade) + (int(assignment) * 2))
        )
    )
