a = float(input('Masukkan nilai a: '))
b = float(input('Masukkan nilai b: '))

assert b !=0, 'kesalahan nilai b tidak boleh 0'

c = a / b
print('%.3f / %.3f = %.3f' % (a, b, c))