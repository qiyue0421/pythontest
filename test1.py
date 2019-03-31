def paixu(s1, s2):
    list_s2 = list(s2)
    pos1 = 0
    if len(s1) == len(s2):
        alive = True
    else:
        alive = False
    while pos1 < len(s1) and alive:
        pos2 = 0
        found = False
        while pos2 < len(list_s2) and not found:
            if s1[pos1] == list_s2[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            list_s2[pos2] = None
        else:
            alive = False
        pos1 += 1
    return alive


print(paixu('python', 'ythonp'))
