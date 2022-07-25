def contrived_func(val):
    if val < 150 and val > 100:
        return True
    elif val * 5 < 361 and val / 2 < 24:
        if val == 6:
            return False
        else:
            return True
    elif val > 75 or val % 2 == 1:
        return True
    else:
        return False
