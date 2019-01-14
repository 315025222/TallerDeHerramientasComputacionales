def diana(x, y):
    if x < 5:
        if y < 10:
            return 3
        if 10 <= y <= 30:
            return 5
        if 30 < y:
            return 3
    if 5 <= x <= 25:
        if y < 10:
            return 7
        if 10 <= y <= 30:
            return 10
        if 30 < y:
            return 7
    if 25 < x:
        if y < 10:
            return 3
        if 10 <= y <= 30:
            return 5
        if 30 < y:
            return 3


