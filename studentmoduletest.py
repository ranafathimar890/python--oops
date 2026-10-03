#this python file is used to test all functionality insidethe student class
#in future that class will be used in real scenario like login/registration 
from modules.student.student import student_details
#step1 : student registration test

email = input("enter your email: ")
password = input("enter your password: ")   

s1=student_details()
s1.setusernameandpassword(email, password)

#step2 : studentlogin test
name=input("enter your full name: ")
date_of_birth=input("enter your date of birth: ")
age=input("enter your age: ")
gender=input("enter your gender: ")
mobile=input("enter your mobile number: ")
language=input("enter your preferred language: ")
school=input("enter your school/college name: ")
class_grade=input("enter your class grade: ")
board=input("enter your board curriculum: ")
academic_year=input("enter your academic year: ")

#set student details
s1.set_student_details(name,date_of_birth, age, gender, mobile, language, school, class_grade, board, academic_year)

#save student details to database
s1.save_basic_details_to_db()
