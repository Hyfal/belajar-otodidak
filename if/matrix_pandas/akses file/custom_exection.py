class ZeroOrNegativeError(RuntimeError):
    def __init__(self, message):
        self.message = message
        
    def printMessage(self):
        print(self.message)
        
def main():
    print('LUAS DAN KELILING LINGKARAN')
    r = float(input('Masukkan jari-jari: '))
    
    try:
        if r <= 0:
            msg = 'Jari-jari tidak boleh bernilai nol atau negatif'
            raise ZeroOrNegativeError(msg)
    except ZeroOrNegativeError as e:
        e.printMessage()
    
    else:
        import math
        luas = math.pi * (r ** 2)
        keliling = 2 * math.pi * r
        print('Keliling = %.3f' % keliling)
        
if __name__ == '__main__':
    main()