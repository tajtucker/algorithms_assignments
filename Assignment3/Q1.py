def C(n):
    if n == 1:
        return 1
    else:
        return C(n-1) + n**3
