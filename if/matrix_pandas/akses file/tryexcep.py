a = float(input('Masukkan nilai a: '))
b = float(input('Masukkan nilai b: '))

try:
    c = a / b
except ZeroDivisionError as e:
    print(e)
    import sys
    sys.exit(1)

print('%.2f / %.2f = %.2f' % (a, b ,c))
