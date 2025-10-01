#4_elif_continue.py
age = int(input("How old are you?"))

if age > 85 and age <= 100:
    print("Very Old")
elif age > 60 and age <= 85:
    print("Old")
elif age > 40 and age <= 60:
    print("Very Adult")
elif age > 30 and age <= 40:
    print("Adult")
elif age > 20 and age <= 30:
    print("Teenager")
elif age > 10 and age <= 20:
    print("Baby")
else:
    print("Invalid")
