def is_striange(s1: int, s2: int, s3: int):
    if s1 >= s2 + s3:
        print("треугольник не получиться")
    elif s2 >= s1 + s3:
        print("треугольник не получиться")
    elif s3 >= s2 + s1:
        print("треугольник не получиться")
    else:
        print("треугольник получается")

section1 = 9
section2 = 5
section3 = 5
is_striange(section1, section2, section3)
