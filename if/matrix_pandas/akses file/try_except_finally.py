f = None
status = True
fileName = input('Masukkan nama file yang akan dibaca:') 

try:
    f = open(fileName)
    data = f.read()
    print(data)
except FileNotFoundError as e:
    status = False 
    print('Kesalahan file \'%s\' tidak ditemukan.' %fileName)
finally:
    if f is not None:
        f.close()
    if not status:
            print('Operasi dibatalkan....')
    else:
            print('Operasi selesai....')


