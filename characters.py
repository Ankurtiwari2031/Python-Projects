data = input("Enter ur data : ")

num = 0
upper = 0
lower = 0
special = 0

for i in data:
    if ord(i) >= 48 and ord(i) <= 57:
        num += 1

    elif ord(i) >= 65 and ord(i) <= 90:
        upper += 1

    elif ord(i) >= 97 and ord(i) <= 122:
        lower += 1

    else:
        special += 1

Total = num + upper + lower + special


print(f" Total numbers : {num}")
print(f" Total capital letters : {upper}")
print(f" Total small letters : {lower}")
print(f" Total special characters : {special}")
print(f" Total characters : {Total}")
