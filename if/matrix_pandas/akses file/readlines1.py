def main():
    f = open('data.txt', 'r')
    data = f.readlines()
    for elemen in data:
        print(elemen, end="")
        f.close()

if __name__ == '__main__':
    main()