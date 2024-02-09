maths = int(input("Input Maths score : "))
if maths >100 :
    print("Invalid score")
elif maths <0 :
    print("Invalid score")
english = int(input("Input English score : "))
if english >100 :
    print("Invalid score")
elif english <0 :
    print("Invalid score")
kiswahili = int(input("Input Kiswahili score : "))
if kiswahili >100 :
    print("Invalid score")
elif kiswahili <0 :
    print("Invalid score")
physics = int(input("Input physics score : "))
if physics >100 :
    print("Invalid score")
elif physics <0 :
    print("Invalid score")
biology = int(input("Input biology score : "))
if biology >100 :
    print("Invalid score")
elif biology < 0 :
    print("Invalid score")
total = maths + english +kiswahili +physics + biology
print(total)
average = total/5
print("YOUR GRADE IS")
if average <40 :
    print("E")
elif average <50:
    print("D")
elif average <60:
    print("C")
elif average <70:
    print("B")
elif average >100:
    print("INVALID")
elif average <0:
    print("INVALID SCORE")
else:print("A")