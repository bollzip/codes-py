def aproxima_pi(n):
    e = 0
    for i in range(0, n):
        e += (((-1)**i)/((2*i)+1))
    return e*4
print(aproxima_pi(10000))