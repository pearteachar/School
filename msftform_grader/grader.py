# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 06:47:00 2018

@author: CWang
"""

import pandas as pd
import matplotlib.pyplot as plt
# =============================================================================
# Client-Side
# Input: 
# - Name of file w/ student answers
# - Answer Key
# - List of classes (names) and a time-range of when the class meets
# =============================================================================
excel_file = 'math_method_class_test.xlsx'

# List of answers
answer_key = ['D', 'C', 'E', 'B', 'A',
              'E', 'D', 'B', 'B', 'A',
              'A', 'A', 'A', 'B', 'C',
              'B', 'E', 'C', 'E', 'A',
              'B', 'B', 'B', 'A', 'D']


# List of classes, separated by time-stamp
classes = ['PreAP CS', 'Reg CS']
time = ['10:00:00', '10:50:00', '13:44:00', '14:30:00']
# =============================================================================
# Back-end Calculations
# =============================================================================
def calc_grades(grades, answer_key):
    student_grade = dict()
    for num in range(1,len(answer_key)+1):
        count = 0   # count holds the number of student who got the question correct
        question = 'Question ' + str(num)
        
        for student, col in grades.iterrows():
            if col[question] == answer_key[num-1]:
                if student in student_grade:
                    student_grade[student] += 4
                else: 
                    student_grade[student] = 4
                count+=1
                
        percent_correct = count/len(student_grade) * 100
        percent_correct = round(percent_correct,2)
        print(question + ': ' +str(percent_correct) + '%')      #Print % students who got the question correct  
    return student_grade
        
df = pd.read_excel(excel_file)  
df = df.set_index('Name')   # Set students as index

# Calculate grades
final = calc_grades(df, answer_key)
plt.hist(final.values())
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.show()
print(final)

#time = df['Start time']
#print(time.iloc[0].hour)
#print(time)


# Calculate grades
#final = calc_grades(df, answer_key)
#print(final)