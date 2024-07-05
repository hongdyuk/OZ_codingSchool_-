from math import pi

def triangle_area(a, b):
    result = a * b * 0.5
    print(f'삼각형의 넓이는 {result}입니다.')

def circle_area(r):
    result = r ** 2 * pi
    print(f'원의 넓이는 {result}입니다.')

def cuboid_area(a, b, c):
    result = a * b * c
    print(f'직육면체의 넓이는 {result}입니다.')
