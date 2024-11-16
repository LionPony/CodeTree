n = int(input())
flag = False
if n % 2 != 0 and n % 3 == 0:
    flag = True
if n % 2 == 0 and n % 5 == 0:
    flag = True
print("true" if flag else "false")