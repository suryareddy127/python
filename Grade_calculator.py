
inp1=int(input("Marks in Maths:"))
inp2=int(input("Marks in Science:"))
inp3=int(input("Marks in English:"))

total_marks = inp1+inp2+inp3
average_marks = total_marks/3
grade = ""
percentage = (total_marks/300)*100
if percentage>=90:
    grade='A+'
elif percentage>=75 and percentage<90:
    grade='A'
elif percentage>60 and percentage<75:
    grade='B'
else:
    grade='C'
print(f"Total Marks:{total_marks},\nAverage Marks:{average_marks},\nGrade:{grade}")

