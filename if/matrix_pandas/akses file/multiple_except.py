def main():
    fileName = input('Masukkan nama file data: ')
    abbr = input('Masukkan singkatan yang dicari: ').upper()

    try:
        f = open(fileName)
        lst = f.read().split('\n')[:-1]

        data = {}
        for e in lst:
            key, val = e.split('=')
            data[key] = val

        print('\n%s singkatan dari %s' % (abbr, data[abbr]))
    except FileNotFoundError:
        print('\nkesalahan file \'%s\' tidak ditemukan.' %fileName)

    except KeyError:
        print('\n%s tidak ditemukan.' % abbr)

if __name__ == '__main__':
    main()