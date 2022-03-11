def perkalian(a,b):
    x = a * b
    for i in range (a-1):
        print(b, end=" + ")
    return x

a = int(input("Masukan Bilangan pertama = "))
b = int(input("Masukan Bilangan kedua = "))
print(b,"=",perkalian(a,b))