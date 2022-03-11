mk = int(input("Berapa jumlah mata kuliah? "))
count = 0
sks = 3
totalpoint = 0
totalsks = sks*mk

for i in range (mk):
    grade = input("Nilai MK "+str(count+1)+" = ")
    count = count +1

    if grade == "A":
        totalpoint += (sks*4)
    elif grade == "B":
        totalpoint += (sks*3)
    elif grade == "C":
        totalpoint += (sks*2)
    elif grade == "D":
        totalpoint += (sks*1)
    
rumus = totalpoint/totalsks
print(round(rumus,2))
