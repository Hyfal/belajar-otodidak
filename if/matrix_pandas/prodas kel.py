def main():
    daftar_mahasiswa = [
        {"nama": "Fahri", "nim": "123456", "kelas": "IF23F", "ipk": 2.6, "penghasilan_orangtua": 1800000},
        {"nama": "Kent", "nim": "123457", "kelas": "IF23F", "ipk": 3.8, "penghasilan_orangtua": 250000},
        {"nama": "Jasmin", "nim": "123458", "kelas": "IF23F", "ipk": 3.2, "penghasilan_orangtua": 100000},
        {"nama": "Naufal", "nim": "123459", "kelas": "IF23F", "ipk": 3.9, "penghasilan_orangtua": 500000},
        {"nama": "Fahri", "nim": "123460", "kelas": "IF23F", "ipk": 3.2, "penghasilan_orangtua": 1800000},
        {"nama": "Husen", "nim": "123461", "kelas": "IF23F", "ipk": 3.6, "penghasilan_orangtua": 2500000},
        {"nama": "Dika", "nim": "123462", "kelas": "IF23F", "ipk": 3.7, "penghasilan_orangtua": 6800000},
        {"nama": "Zamzami", "nim": "123463", "kelas": "IF23F", "ipk": 3.3, "penghasilan_orangtua": 7000000},
        {"nama": "Hidayat", "nim": "123464", "kelas": "IF23F", "ipk": 3.1, "penghasilan_orangtua": 1800000},
        {"nama": "Nurdin", "nim": "123465", "kelas": "IF23F", "ipk": 3.8, "penghasilan_orangtua": 1500000},
    ]
    nama_penerima_beasiswa_prestasi = []
    nama_penerima_beasiswa_ekonomi = []
    kriteria_beasiswa_prestasi = {"ipk": 3.5}
    kriteria_beasiswa_ekonomi = {"penghasilan_orangtua": 2000000}

    while True:
        print("\n--- Program Beasiswa ---")
        print("1. List Nama Mahasiswa")
        print("2. Cek Penerima Beasiswa")
        print("3. List Penerima Beasiswa")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            list_nama_mahasiswa(daftar_mahasiswa)
        elif pilihan == '2':
            cek_penerima_beasiswa(daftar_mahasiswa, nama_penerima_beasiswa_prestasi, nama_penerima_beasiswa_ekonomi, kriteria_beasiswa_prestasi, kriteria_beasiswa_ekonomi)
        elif pilihan == '3':
            list_penerima_beasiswa(nama_penerima_beasiswa_prestasi, nama_penerima_beasiswa_ekonomi)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

def list_nama_mahasiswa(daftar_mahasiswa):
    print("\nList Nama Mahasiswa:")
    for i, mahasiswa in enumerate(daftar_mahasiswa, 1):
        print(f"{i}. {mahasiswa['nama']} (NIM: {mahasiswa['nim']}, Kelas: {mahasiswa['kelas']})")

def cek_penerima_beasiswa(daftar_mahasiswa, nama_penerima_beasiswa_prestasi, nama_penerima_beasiswa_ekonomi, kriteria_beasiswa_prestasi, kriteria_beasiswa_ekonomi):
    nama_penerima_beasiswa_prestasi.clear()
    nama_penerima_beasiswa_ekonomi.clear()
    for mahasiswa in daftar_mahasiswa:
        if mahasiswa["ipk"] >= kriteria_beasiswa_prestasi["ipk"]:
            nama_penerima_beasiswa_prestasi.append(f"{mahasiswa['nama']} (NIM: {mahasiswa['nim']}, Kelas: {mahasiswa['kelas']})")
        if mahasiswa["penghasilan_orangtua"] <= kriteria_beasiswa_ekonomi["penghasilan_orangtua"]:
            nama_penerima_beasiswa_ekonomi.append(f"{mahasiswa['nama']} (NIM: {mahasiswa['nim']}, Kelas: {mahasiswa['kelas']})")
    print("\nPenerima beasiswa (Golongan Prestasi):")
    for i, nama in enumerate(nama_penerima_beasiswa_prestasi, 1):
        print(f"{i}. {nama}")
    print("\nPenerima beasiswa (Golongan Ekonomi):")
    for i, nama in enumerate(nama_penerima_beasiswa_ekonomi, 1):
        print(f"{i}. {nama}")

def list_penerima_beasiswa(nama_penerima_beasiswa_prestasi, nama_penerima_beasiswa_ekonomi):
    print("\nList Penerima Beasiswa (Golongan Prestasi):")
    for i, nama in enumerate(nama_penerima_beasiswa_prestasi, 1):
        print(f"{i}. {nama}")
    print("\nList Penerima Beasiswa (Golongan Ekonomi):")
    for i, nama in enumerate(nama_penerima_beasiswa_ekonomi, 1):
        print(f"{i}. {nama}")

if __name__ == "__main__":
    main()
