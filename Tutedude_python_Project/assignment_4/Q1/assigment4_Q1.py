
def Read():

      Sample_File = open("Sample.txt","r")
      for line in Sample_File:
        print(line)
      Sample_File.close()
      return line

def CountLines():
   try:
    Sample_File = open("Sample.txt","r")
    Line_Count = 0
    for line in Sample_File:
      Line_Count += 1
      print("line",Line_Count,":", line)
    Sample_File.close()
   except FileNotFoundError:
     print("\nthe File Sample.txt was not found")

CountLines()