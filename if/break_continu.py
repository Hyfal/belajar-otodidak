print("====================================")
print("Belajar penggunaan break & Continue")
print("====================================")

a = 1 
while a < 11:
    if a == 4:
        print("4 tidak dicetak karena semua baris dilewati")
    if  a > 8:
        print("a lebih besar dari 8, maka program keluar dari while")
        break

    print(a)
    a = a + 1
