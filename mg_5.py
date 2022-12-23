k1 = 23000
k2 = 69000

V = 11 / 1000
print('V',V)

ro = 1800

m = V * ro
print('масса цилиндра',m)

P = 9.8 * m

print('p = ',P)


dL1 = (9.8 * m)/k1
dL2 = (9.8 * m)/k2

print('dL1',dL1)
print('dL2',dL2)


dL = dL1 + dL2

print('резултат',dL)