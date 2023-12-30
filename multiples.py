# Leah Alcaraz 301279925 October 6, 2023

fNum1, fNum2 = map(int, input('Enter two numbers that are smaller than 0 or greater than 10: ').split())
fNum1 = int(fNum1)
fNum2 = int(fNum2)

if (fNum1 < 0 or fNum1 > 10) or (fNum2 < 0 or fNum2 > 10):
    print("Both numbers are valid")
else:
    print("Invalid")

print("\b")

sNum1, sNum2 = map(int, input('Enter two numbers that are smaller than 0 or greater than 10: ').split())
sNum1 = int(sNum1)
sNum2 = int(sNum2)

if (sNum1 < 0 or sNum1 > 10) or (sNum2 < 0 or sNum2 > 10):
    print("Second number(",sNum2,") is invalid")
else:
    print("Invalid")

print("\b")

tNum1, tNum2 = map(int, input('Enter two numbers that are smaller than 0 or greater than 10: ').split())
tNum1 = int(tNum1)
tNum2 = int(tNum2)

if (tNum1 < 0 or tNum1 > 10) or (tNum2 < 0 or tNum2 > 10):
    print("First number(",tNum1,") is invalid")
else:
    print("Invalid")

print("\b")

lNum1, lNum2 = map(int, input('Enter two numbers that are smaller than 0 or greater than 10: ').split())
lNum1 = int(lNum1)
lNum2 = int(lNum2)

if (lNum1 < 0 or lNum1 > 10) or (lNum2 < 0 or lNum2 > 10):
    print("Both numbers are valid")
else:
    print("Both number are invalid")
