numGrades=int(float(input('How many numbers do you have? ')))
grades=[]
for i in range (0, numGrades,1):
    grade=float(input('Please enter your grade: ' ))
    grades.append(grade)
for i in range(0,numGrades,1):
    print(grades[i])
print('Thank you')
