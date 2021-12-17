def is_triangle(a, b, c):
    if b+c < a:
        print("Noa")
    elif a + c < b:
        print("Nob")
    elif a+ b < c:
        print("Noc")
    else:
        print("Yesc")

is_triangle(3,4,2)
