# 1. Age Group Categorization
# Classify a person's age group : child(<13), Teenagers(13-19), Adult(20-59), Senior(60+).

age = 60

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")