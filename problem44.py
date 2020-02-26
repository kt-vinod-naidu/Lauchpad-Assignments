def rem(dup):
  list=[]
  for num in dup:
    if num not in list:
      list.append(num)
  return list
dup=[1,23,34,34,54,65,65,65]
print(rem(dup))