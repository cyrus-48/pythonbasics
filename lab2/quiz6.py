# Write a program that prompts the user to enter a letter grade A/a, B/b, C/c, D/d, or F/f and displays its corresponding numeric value 4, 3, 2, 1, or 0.

def checkGrade(grades: list, grade) -> int:
    for i in range(len(grades)):
        if grade.upper() == grades[i]:
            print('The numeric value for grade ', grade, ' is ', 4 - i)
            return 4 - i
            break

    else:
        print("is an invalid grade")


grades: list = ['A', 'B', 'C', 'D', 'F']
grade = input("Enter a Letter Grade: ")

checkGrade(grades, grade)
