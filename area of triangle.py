# Three sides of the triangle is a,b and c
a=float(input('Enter first side:'))
b=float(input('Enter second side:'))
c=float(input('Enter third side:'))
#calculate tje side of triangle
s=(a+b+c)/2
#calculate the area
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is% 0.3f'%area)
