from collections import deque
class AntrianPesanan:
    def __init__(self):
        self.pesanan = deque()

    def tambah_pesanan(self, nama_pesanan):
        self.pesanan.append(nama_pesanan)
        print(f'Masukan Nama Pesanan : {nama_pesanan}')
        print(f'"{nama_pesanan}" Berhasil ditambahkan ke antrian pesanan')

    def lihat_antrian(self):
        if self.pesanan:
            print("Daftar antrian saat ini:", list(self.pesanan))

    def menghapus_pesanan_di_depan(self):
        self.pesanan.popleft()
        print(f' antrian pesanan: "{self.antrian[0]}"')

def utama():
    AntrianPesanan = AntrianPesanan()
    
    while True:
        print("Pilihan:")
        print("1. Tambah Pesanan")
        print("2. Menghapus Antrian")
        print("3. Lihat Antrian")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan: ")
        
        if pilihan == '1':
            nama_pesanan = input("Masukkan Nama Pesanan: ")
            AntrianPesanan.tambah_antrian(nama_pesanan)
        elif pilihan == '2':
            AntrianPesanan.menghapus_pesanan_di_depan()
        elif pilihan == '3':
            AntrianPesanan.lihat_antrian()
        
        
    
