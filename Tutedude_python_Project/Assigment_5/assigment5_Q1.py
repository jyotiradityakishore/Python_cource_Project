

Student_detal = {"jon":34,"akash":64, "sita":73, "mohan":94}      #  student detal 
User_Input = input("Enter the student's name: ")                  #  taking input from  user


if User_Input in Student_detal:
    print(User_Input,"Marks:",Student_detal[User_Input])          # compairing user input to student_detal
else:
    print(User_Input,"Student Not found")


