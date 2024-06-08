class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

# Fungsi untuk menginput data mahasiswa
def input_mahasiswa():
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
    mhs = []
    for i in range(jumlah_mahasiswa):
        nama = input(f"Masukkan nama mahasiswa ke-{i+1}: ")
        umur = int(input(f"Masukkan umur mahasiswa ke-{i+1}: "))
        mahasiswa = Mahasiswa(nama, umur)
        mhs.append(mahasiswa)
    return mhs

# Fungsi untuk mencari mahasiswa berdasarkan umur
def cari_mahasiswa_berumur(mahasiswas, umur_dicari):
    mahasiswa_ditemukan = False
    print(f"Mahasiswa berumur {umur_dicari} ditemukan:")
    for mahasiswa in mahasiswas:
        if mahasiswa.umur == umur_dicari:
            print("Nama:", mahasiswa.nama)
            print("Program Studi Teknik Informatika Universitas Buana Perjuangan Karawang")
            print("Umur:", mahasiswa.umur)
            mahasiswa_ditemukan = True
    if not mahasiswa_ditemukan:
        print("Tidak ada mahasiswa yang berumur", umur_dicari)

if __name__ == "__main__":
    mhs = input_mahasiswa()
    umur_dicari = int(input("Masukkan umur yang ingin dicari: "))
    cari_mahasiswa_berumur(mhs, umur_dicari)
