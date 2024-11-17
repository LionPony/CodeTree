y = int(input())
yoon = False
if y % 4 == 0:
    if not (y % 100 == 0 and y % 400 != 0):
        yoon = True
print("true" if yoon else "false")