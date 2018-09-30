print("addition : 1")
print("subtraction : 2")
print("multiplication : 3")
print("division : 4")
print("exit : 5")

ch = int(input("enter your choice"))

if ch >= 1 and ch <= 4:
    print("enter two numbers to perform the operation")
    a = int(input())
    b = int(input())
    if ch == 1:
        c = int(a + b)
        print("result : ", c)
    elif ch == 2:
        c =int(a - b)
        print("result : ", c)
    elif ch == 2:
        c =int(a * b)
        print("result : ", c)
    elif ch == 2:
        c =int(a / b)
        print("result : ", c)
elif ch == 5:
        exit()
else:
    print("invalid choice")

