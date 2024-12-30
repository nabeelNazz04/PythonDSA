def get_squared_numbers(numberes):
  squared=[]
  for i in numberes:
    squared.append(i*i)
  return squared
number=[1,4,5,6]
squared=get_squared_numbers(number)
print(squared)
