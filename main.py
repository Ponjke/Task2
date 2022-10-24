'''
input_str1 = '10'
input_str2 = '10 20'
input_str3 = '10 20 30'
'''
input_string = input()
values = input_string.split()
count = len(values)
if count == 1:
    a = input_string
    if a <= 0:
        print("There is no circle")
    else:
        p = (2 * 3.14 * a)
        s = (3.14 * a**2)
        print(f"Circle:  {a=}; {p=} {s=}")
elif count == 2:
    a, b = values
    a = int(a)
    b = int(b)
    if a <= 0 or b <= 0:
        print("There is no square")
    else:
        p = ((a + b) * 2)
        s = (a * b)
        print(f"Square: {a=}  {b=}; {p=} {s=}")
elif count == 3:
    a, b, c, h = values
    a = int(a)
    b = int(b)
    c = int(c)
    h = int(h) #Висота
    if a <= 0 or b <= 0 or c <= 0:
        print("There is no triangle")
    elif a + b <= c or c + a <= b or c + b <= a:
        print("There is no triangle")
    else:
        p = (a + b + c)
        s = (1/2 * c * h)
        print(f"Triangle: {a=} {b=} {c=}; {p=} {s=}")


a = input_string  # '10'
a , b = values  # '10 20'
a, b, c = values  # '10 20 30'
