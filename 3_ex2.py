def print_odd(n):
  odd=[]
  for i in range(1,n):
    if i%2 !=0:
      odd.append(i)
  return odd
x=int(input("Enter a max number"))
odd=print_odd(x)
print(odd)
