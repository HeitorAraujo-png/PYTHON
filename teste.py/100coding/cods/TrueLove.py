def calculate_love_score(name, name2):
    t = r = u = e = l = o = v = e = 0
    for letter in name:
        if letter in 'Tt':
            t += 1
        elif letter in 'Rr':
            r += 1
        elif letter in 'Uu':
            u += 1
        elif letter in 'Ee':
            e += 1
    for letter in name:
        if letter in 'Ll':
            l += 1
        elif letter in 'Oo':
            o += 1
        elif letter in 'Vv':
            v += 1
        elif letter in 'Ee':
            e += 1
    for letter in name2:
        if letter in 'Tt':
            t += 1
        elif letter in 'Rr':
            r += 1
        elif letter in 'Uu':
            u += 1
        elif letter in 'Ee':
            e += 1
    for letter in name2:
        if letter in 'Ll':
            l += 1
        elif letter in 'Oo':
            o += 1
        elif letter in 'Vv':
            v += 1
        elif letter in 'Ee':
            e += 1
    x = t + r + u + e
    y = l + o + v + e
    print(f'{x}{y}')
calculate_love_score("Angela Yu", "Jack Bauer")