def bagi(a, b):
    if not (isinstance(a, float) or isinstance(a, int)):
        raise ValueError('Nilai a harus bertipe bilangan')
    if not (isinstance(b, float) or isinstance(b, int)):
        raise ValueError('Nilai b harus bertipe bilangan')
    if b == 0:
        raise ZeroDivisionError('Terjadi pembagian dengan 0')
    
    return a / b

def main():
    try:
        c = bagi(6.0, 3)
        print(c)
        
    except ZeroDivisionError as e:
        print(e)
        
if __name__ == '__main__':
    main()