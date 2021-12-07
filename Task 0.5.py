# Three triangle lenghts x,y,z:  
x = float(5)  
y = float(6)  
z = float(8)  
  
# determine half of the perimeter  
s = (x + y + z) / 2  
  
def triangle():
    area = (s*(s-x)*(s-y)*(s-z)) ** 0.5  
    print('The area of the triangle is %0.2f' %area)

triangle()