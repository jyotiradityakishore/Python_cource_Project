
Text_Storage = open("output.txt", 'w')
User_Text = input("Enter text you want to write to file:")                  # writing data to output.txt
Text_Storage.write(User_Text +"\n")
print("Data written successfully")
Text_Storage.close()


Text_Storage = open("output.txt", 'a')
User_Text_Append = input("Enter additional text to append:")               # appending data to output.txt
Text_Storage.write(User_Text_Append + "\n")                                # it took me 2H to just find how to append data to next line this way cource should mention this small things  
print ("data written successfully")                                        # 	ಠ__ಠ
Text_Storage.close()

Text_show = open("output.txt","r")
Text_Read = Text_show.read()
print("Final content of Text_Read is:")                                   # reading data from output.txt
print(Text_Read)
Text_show.close()

