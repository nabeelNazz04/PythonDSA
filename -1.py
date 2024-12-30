print(4*5)
print(2**2)#power
time=8.9999999
print(round(time,2))#rounding offf
#strings 
text="Nazz"
print(text[0])
#text[0]="L" throw error czzz strings are immutable
print(text[0:3])
#joining number to a string
num=9
s="Hello #"
print(s+str(num))

#list

item=["food","Water","Clothes"]
print(item)
print(item[0])
item[0]="Chips"
print(item)
item.append("Food")
print(item)
item.insert(1,"Shelter")
print(item)
a=["a","b","c"]
b=["c","d"]
c=a+b
print(c)
print("a"in c)#whether "a"is in c

#if statement

a=input("Enter a no:")
a=int(a)#to convert string a to num
if a%2==0:
  print("Number is even")
else:
  print("Number s odd")