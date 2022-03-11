a = int(input("Masukan batas bawah = "))
b = int(input("Masukan batas atas = "))

def ganjil(a,b):
    if a > b :
        for i in reversed(range(b,a+1)):
            if i % 2 == 1:
                print(i, end= " ")
    else:
        for i in range (a, b+1):
            if i % 2 == 1:
                print(i, end = " ")

ganjil(a,b)