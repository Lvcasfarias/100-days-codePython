from re import X
import struct


student_heights = input('Input a list of Students height ').split()
for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    #print(student_heights[n])

# 165 173 189 169 146
y = 0
for x in student_heights:
    student_heights.append(x)
    y += 1
    if y == x:
        print(f'{y} ESTE É O X')
        break
        