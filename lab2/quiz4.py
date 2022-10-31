# Given variables first and last, each of which is associated with a string, representing a first and a last name,
# respectively. Write an expression whose value is a string that is a full name of the form "Last, First". So,
# if first were associated with "alan" and last with "turing", then your expression would be "Turing,Alan". (Note the
# capitalization! Note: no spaces!) And if first and last were "Florean" and "fortescue" respectively,
# then your expression's value would be "Fortescue,Florean".

def formattedString(first: str, last: str) -> str:
    return last.capitalize() + first.capitalize()


first: str = input("Enter first name :")
last: str = input("Enter last name : ")

myString = formattedString(first, last)
