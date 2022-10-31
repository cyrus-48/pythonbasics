
#Write a program that prompts the user to enter a letter grade A/a, B/b, C/c, D/d, or F/f and displays its corresponding numeric value 4, 3, 2, 1, or 0.
grades = ['A','B','C','D','F']

grade = input("Enter a Letter Grade: ")

for i in range(len(grades)):
    if grade.upper() == grades[i]:
        print('The numeric value for grade ', grade, ' is ',4 - i)
        break;
    else:
        print(grade, "is an invalid grade")