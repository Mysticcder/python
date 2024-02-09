print("Grades calculator")
math = int(input("math: "))
eng = int(input("eng: "))
phyc = int(input("phyc: "))
kis = int(input("kis: "))
hist = int(input("hist: "))
total = math + eng + phyc + kis + hist
avg= total/5
print("avg")
if avg >= 0 and  avg <= 39:
    print("E")
elif avg > 40 and  avg < 50:
    print("D")
elif avg > 51 and avg < 60:
    print("C")
elif avg > 61 and avg < 70:
    print("B")
elif avg > 71 and avg < 100:
    print("A")
elif avg > 100:
    print("invalid input")
elif avg < 0:
    print("invalid input")
