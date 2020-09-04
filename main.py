
grade = str(input("Enter your course 1 letter grade: "))
g = str(grade)
credit = float(input("Enter your course 1 credit: "))
c = int(credit)

if g == 'A':
  gp = 4.0
  print("Grade point for course 1 is: ",gp)
elif g == 'A-':
  gp = 3.67
  print("Grade point for course 1 is: ",gp)
elif g == 'B+':
  gp = 3.33
  print("Grade point for course 1 is: ",gp)
elif g == 'B':
  gp = 3
  print("Grade point for course 1 is: ",gp)
elif g == 'B-':
  gp = 3.67
  print("Grade point for course 1 is: ",gp)
elif g == 'C+':
  gp = 2.33
  print("Grade point for course 1 is: ",gp)
elif g == 'C':
  gp = 2
  print("Grade point for course 1 is: ",gp)
elif g == 'D':
  gp = 1
  print("Grade point for course 1 is: ",gp)
else:
  gpa = 0
  print("Grade point for course 1 is: ",gp)
