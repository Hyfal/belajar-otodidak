def main():
    f = open('data1.txt', 'w')

    data = ['python\n', 'C++\n', 'PHP\n', 'Ruby\n']
    f.writelines(data)
    f.close
if __name__ == '__main__':
    main()