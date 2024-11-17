mid, end = map(int, input().split())
scholarship = 0
if mid >= 90:
    if end >= 95:
        scholarship += 100000
    elif end >= 90:
        scholarship += 50000
print(scholarship)