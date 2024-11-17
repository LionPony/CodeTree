mid, end = map(int, input().split())
scholarship = 0
quilfy = False
if mid >= 90:
    quilfy = True
if quilfy:
    if end >= 95:
        scholarship += 100000
    elif end >= 90:
        scholarship += 50000
print(scholarship)