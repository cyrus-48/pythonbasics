# In this coding exercise, you are asked to write the body of a function called grade_stats that accepts as a parameter a list representing the grades given in a course and returns a dictionary mapping each grade to the count of how many were given.

# The grades may not always be A, B, C, D, E, and I. 
# For example, A- is a valid grade in some places as is 3.7. 
# You should treat whatever is in the passed-in list as a valid grade.
G = ['A', 'I', 'C', 'C', 'E', 'B', 'A', 'E', 'E', 'A', 'B', 'B', 'B'] 

def grade_stats(lis):
  # If the passed-in list is empty, your function should return an empty dictionary.
  
  # Insert your code here
    if len(lis) == 0:
        return {}
    else:
        return {i:lis.count(i) for i in lis}
print(grade_stats(G))