x=int(input ("enter year of birth:"))
age= 2019-x
print(age)
if age < 18:
     print("minor")
if age > 36:
    print("elder")
if age in list(range(18, 37)):
    print("youth")