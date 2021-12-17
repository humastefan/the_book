"""Teorema lui Fermat"""
a = int(input("Baga a-ul te rog:"))
b = int(input("Baga b-ul te rog:"))
c = int(input("Baga c-ul te rog:"))
n = int(input("Baga n-ul te rog:"))
def check_fermat(a, b, c, n):
    for n in range(10):
        if a**n + b**n == c**n and n>2:
            print(a**n + b**n, "este egal cu", c**n)
            print("holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work.")
            print(a ** n + b ** n, "nu este egal cu", c ** n)
            #return

check_fermat(a, b, c, n)