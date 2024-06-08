def main():
    f = open('data.txt', 'r')
    data = f.readlines()
    print(data)
    f.close()
if __name__ == '__main__':
    main()