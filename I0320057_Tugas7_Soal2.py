import math
def soaldua(a,b):
    print("a = ", a)
    print("b = ", b)
    print('---'*4)

    print('1.Abs')
    print('Nilai mutlak a dan b adalah')
    print("|a| = ", abs(a))
    print("|b| = ", abs(b))

    print('\n2.min and max')
    print('nilai terbesar = ', max(a,b))
    print('nilai terkecil = ', min(a,b))

    print('\n3.ceil')
    print("a = ", a)
    print("b = ", b)
    print("math a ceil : ", math.ceil(a))
    print("math b ceil : ", math.ceil(b))

a = float(input('Masukkan nilai a = '))
b = float(input('Masukkan nilai b = '))
soaldua(a,b)