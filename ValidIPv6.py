def valid(x):
    v = 'ABCDEFabcdef0123456789'
    n = x.split(':')
    if len(n)!=8:
        return False
    for i in n:
        if len(i)>4:
            return False
        for j in i:
            if j not in v:
                return False
            else:
                continue
    return True

print(valid('3FFE::1:200:F8FF:FE75:50DF'))
