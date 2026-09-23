a = input("Enter word : ")
c = ""
for i in range(len(a) - 1, -1, -1):
    c += a[i]
if c == a:
    print(f"{a} is a palindrome.")
else:
    print(f"{a} is not a palindrome.")
