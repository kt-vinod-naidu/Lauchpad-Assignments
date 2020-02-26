def rem(dup):
  list=[]
  for num in dup:
    if num not in list:
      list.append(num)
  return list
dup=[1,2,2,3,4,4,5,6,7,7,8,9]
print(rem(dup))