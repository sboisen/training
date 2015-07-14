def consonantalify(s):
    base = ''
    for c in s:
        if c not in 'aeiouAEIOU ':
            base += c
    return base
