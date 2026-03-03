# 9. Leap year checker
# Problem: if a year is a leap year. (Leap year are divisible by 4, but not by 100 unless also divible by 400)

year = 2026

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is leap year")
else:
    print(year,"is NOT leap year")