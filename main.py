'''
input_str1 = '10'
input_str2 = '10 20'
input_str3 = '10 20 30'
'''
import math

input_string = input()
values = input_string.split()
count = len(values)
if count == 1:
    a = input_string
    if a <= 0:
        print("There is no circle")
    else:
        perimeter = (2 * 3.14 * a)
        area = (3.14 * a ** 2)
        print(f"Circle:  {a=}; {perimeter=} {area=}")
elif count == 2:
    a, b = values
    a = int(a)
    b = int(b)
    if a <= 0 or b <= 0:
        print("There is no square")
    else:
        perimeter = ((a + b) * 2)
        area = (a * b)
        print(f"Square: {a=}  {b=}; {perimeter=} {area=}")
elif count == 3:
    a, b, c = values
    a = int(a)
    b = int(b)
    c = int(c)
    if a <= 0 or b <= 0 or c <= 0:
        print("There is no triangle")
    elif a + b <= c or c + a <= b or c + b <= a:
        print("There is no triangle")
    else:
        perimeter = (a + b + c)
        area = math.sqrt(perimeter * (perimeter - a) * (perimeter - b) * (perimeter - c))
        print(f"Triangle: {a=} {b=} {c=}; {perimeter=} {area=}")