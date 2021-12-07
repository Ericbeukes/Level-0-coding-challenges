# Get three triangle lenghts from user x,y,z:  
x = float(5)  
y = float(6)  
z = float(7)  
  
# determine half of the perimeter  
s = (x + y + z) / 2  
  
# calculate the area of triangle 
area = (s*(s-x)*(s-y)*(s-z)) ** 0.5  
print('The area of the triangle is %0.2f' %area)