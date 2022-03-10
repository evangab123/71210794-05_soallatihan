a = int(input("Masukan batas atas = "))
b = int(input("Masukan batas bawah = "))

def ganjil(a,b):
    if a > b :
        for i in range (b+1, a+1):
            if i % 2 == 1:
                print(i, end = " ")
    elif a < b:
        for i in reversed(range(a+1,b+1)):
            if i % 2 == 1:
                print(i, end= " ")

ganjil(a,b)