# Develpoe python program using numpy

import numpy as np 
students = np.array(["s1","s2","s3","s4","s5"])

# Mid Semester Examinatiion Marks
mid_marks = np.array([
    [65,70,68,72],  #s1
    [78,75,80,77],  #s2
    [55,60,58,62],  #s3
    [82,85,80,88],  #s4
    [70,68,72,74]   #s5
])
# End Semester Examination Marks
end_marks = np.array([
    [72,78,75,80],  #s1
    [84,82,86,83],  #s2
    [65,68,66,70],  #s3
    [88,90,85,92],  #s4
    [78,75,80,82]   #s5
])

# Total Marks
total_mid_marks = np.sum(mid_marks,axis=1)
total_end_marks = np.sum(end_marks,axis=1)

# Average
mid_average = np.mean(mid_marks,axis=1)
end_average = np.mean(end_marks,axis=1)

#percentage Implement
percentage_implement = ((total_end_marks - total_mid_marks)/total_mid_marks)*100

# Display
print("Students Record")
print("-" *80)
print("student\tmid total\tend total\tmid ave\t\tend ave\t  % implement")
print("-" *80)
for i in range(len(students)):
    print(f"{students[i]}\t{total_mid_marks[i]}\t\t{total_end_marks[i]}"
    f"\t\t{mid_average[i]:.2f}\t\t{end_average[i]:.2f}"
    f"\t\t{percentage_implement[i]:.2f}%")