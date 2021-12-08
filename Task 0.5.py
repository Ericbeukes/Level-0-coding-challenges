def triangle(x,y,z):
    s = (x + y + z) / 2  
    area = (s*(s-x)*(s-y)*(s-z)) ** 0.5  
    print('The area of the triangle is %0.2f' %area)

triangle(7,8,9)