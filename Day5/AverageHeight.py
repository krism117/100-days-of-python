total_students = 0
total_height = 0
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total_students += 1
  total_height += student_heights[n]
average_height = total_height/total_students
print(average_height)
