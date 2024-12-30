x=input("Enter no.1:")
y=input("Enter no.2:")
x=int(x)
y=int(y)
try:
  z=x/y
except ZeroDivisionError as e:
  print("Exception occured:",e)
  z=None
print("Result:",z)