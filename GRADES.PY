from audioop import avg


numGrades=int(float(input('How many numbers do you have? ')))
grades=[]
bucket=0
for i in range (0, numGrades,1):
    grade=float(input('Please enter your grade: ' ))
    grades.append(grade)
for i in range(0,numGrades,1):
    print(grades[i])
print('Thank you')
for i in range(0,numGrades,1):
    bucket=bucket+grades[i]
Average=bucket/numGrades
print('Your average is: ', Average)

for i in range(0,numGrades,1):
    grades.sort()
print('Largest element is ', grades[i])

for i in range(0,numGrades,1):
    grades.sort()
    lowvalue=min(grades)
print('Lowest number is ', lowvalue)
