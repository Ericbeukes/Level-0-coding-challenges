def maximum(a, b, c, d):
  
    if (a >= b) and (a >= c) and (a >= d):
        largest = a
    elif (b >= a) and (b >= c) and (b >= d):
        largest = b
    elif (c >= a) and (c >= b) and (c >= d):
        largest = c
    else:
        largest = d
          
    return largest
  
# Test code with numbers 
a = 1
b = 22
c = 3
d = 2
print(maximum(a, b, c, d))