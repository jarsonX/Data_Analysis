# Create a summary of confusion matrices from directory.

# 1) Create an empty matrix which will store the summary.
# 2) Learn names of all the files in directory and store them in a list.
# 3) Iterate through all the files:
    # 3.1) Load by lines.
    # 3.2) Find index of string ‘=== Confusion Matrix ===\n’.
    # 3.3) Slice everything till the end.
    # 3.4) Divide the lines by '|'.
    # 3.5) Divide the first part of the line by whitespaces.
    # 3.6) Convert each element to int.
    # 3.7) Add each element as a row in the confusion matrix.
    # 3.8) Add the confusion matrix to the summary.
# 4) Print results.

import os

def print_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str,row)))

# Used at the end of confusion_matrix function. Adds a newly created matrix to
# a Summary Confusion Matrix.
def add_matrix(matrix, SCM_sum):
    # At the first iteration, SCM is empty. So we create an empty matrix to
    # begin with. Each next matrix (taken from a file) will be added to this one.
    if len(SCM_sum) == 0:  
        # We still haven't added any matrix but we already now that is has 11 
        # elements.
        n = len(matrix)  # Each matrix has 11 elements.
        # Therefore we create a matrix with 11 empty slots (i.e. 0s)
        # Below it is simply stated: Fill n slots with 0s n times.
        # This gives a 11 x 11 matrix comprised of 0s.
        SCM_sum = [[0 for _ in range(n)] for _ in range(n)]
        # SCM_sum now has 11 elements (0s).
  
    # Given that the empty matrix is ready, we can start to fill it with numbers.
    # r stands for 'row', and 'c' for column.
    for r in range(len(SCM_sum)):
            for c in range(len(SCM_sum[r])):
                SCM_sum[r][c] += matrix[r][c]
  
    return SCM_sum

# Creates a Summary Confusion Matrix ('SCM')
def confusion_matrix(path):
    files_list = [os.path.join(path, name) for name in os.listdir(path)
                  if os.path.isfile(os.path.join(path,name))]
    
    SCM = []  # SCM we're building.
    
    # Creates a matrix for each file (total of 30 files).
    for a_file in files_list:
        lines = open(a_file).readlines()
        index = lines.index("=== Confusion Matrix ===\n") + 3  # Here a matrix starts.
        
        matrix = []  # The matrix we're building. Resets to [] for each loop.
        
        # Creates a list that represents Confusion Matrix.
        # The list comprises elements which are lines from the Confusion Matrix (11 elements)
        # A separate matrix is created for each file (total of 30 matrices).
        while "|" in lines[index]:
            line = lines[index]  # The actual line in the loop.
            line = line.split("|")  # Split the line by "|". Creates a 2-elements list.
            line = line[0].split()  # Take only the first element.
            line = list(map(int, line))  # List is comprised of strs. We convert those to ints. 
                                         # Otherwise it would be impossible to sum them.
                                         
            matrix.append(line)  # Here the line goes to our matrix created for that file.
            index += 1          
          
            # Shows each matrix with a file name.
            # print(a_file)
            # print(matrix)            
          
        SCM = add_matrix(matrix, SCM)  # The matrix goes into SCM and we are ready
                                       # to start over with the while loop.
    return SCM
            
matrix = confusion_matrix(r"C:\Users\...\data")
print_matrix(matrix)

