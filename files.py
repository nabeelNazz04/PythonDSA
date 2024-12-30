f=open("C:\\Data\\funny.txt","w")#w mode always overright the code
f.write("iiiii am Nabeeeeeeeel")
f.close()
f=open("C:\\Data\\funny.txt","a")#a mode for append
f.write("\nHei there")
f.close()
f=open("C:\\Data\\funny.txt","r")#r for read
print(f.read())
f.close()
f=open("C:\\Data\\funny.txt","r")
for line in f:
  print(line)
f.close()