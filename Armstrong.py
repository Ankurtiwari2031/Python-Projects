try:
    a = input("Enter no : ")
    p = len(a)
    l = []
    n = 0
    for i in range(0, len(a)):
        l.append(a[i])

    for x in l:
        m = int(x) ** p
        n += m

    if n == int(a):
        print(f"{a} is a Armstrong num !!")
    else:
        print(f"{a} is Not an Armstrong num !!")

except:
    print("Hey user ! you get an error !")
