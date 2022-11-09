n = int(input("Enter no.of Element in list: "))
list = [] for i in range(n):    
  x = int(input("Enter list: "))   
  list.append(x) print(list) 
  a = max(list) 
  b = min(list) 
  print(a, b)
  c = list.index(a) 
  d = list.index(b) 
list[c], list[d] = list[d], list[c]
print(list) 
 
