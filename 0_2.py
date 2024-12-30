a=["a","b","c"]
b=["d","e","f"]
c=["g","h","i"]

char=input("Enter a charecter")
if char in a:
  print("a")
elif char in b:
  print("b")
elif char in c:
  print("c")
else:
  print("Not found")