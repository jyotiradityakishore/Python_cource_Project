
Text_Storage = open("output.txt", 'w')
User_Text = input("Enter text you want to write to file:")
Text_Storage.write(User_Text +"\n")
print("Data written successfully")
Text_Storage.close()


Text_Storage = open("output.txt", 'a')
User_Text_Append = input("Enter additional text to append:")
Text_Storage.write(User_Text_Append + "\n")
print ("data written successfully")
Text_Storage.close()

Text_show = open("output.txt","r")
Text_Read = Text_show.read()
print("Final content of Text_Read is:")
print(Text_Read)
Text_show.close()

