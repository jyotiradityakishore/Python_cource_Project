

Student_detal = {"jon":34,"akash":64, "sita":73, "mohan":94}      #
User_Input = input("Enter the student's name: ")                  #


if User_Input in Student_detal:
    print(User_Input,"Marks:",Student_detal[User_Input])          #
else:
    print(User_Input,"Student Not found")


