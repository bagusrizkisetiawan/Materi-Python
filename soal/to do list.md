```python
# Inisialisasi list kosong untuk menyimpan daftar kegiatan
kegiatan = []

print("===== Selamat Datang di Aplikasi Daftar Kegiatan! =====")

# Perulangan utama program yang akan berjalan selamanya
while True:
    print("\n--- MENU ---")
    print("1. Tambah Kegiatan")
    print("2. Tampilkan Kegiatan")
    print("3. Hapus Kegiatan")
    print("4. Keluar")

    # Meminta pilihan dari pengguna
    pilihan = input("Pilih menu (1/2/3/4): ")

    # Logika percabangan berdasarkan pilihan pengguna
    if pilihan == '1':
        # Blok untuk menambah kegiatan (INI SUDAH BERFUNGSI DENGAN BAIK)
        kegiatan_baru = input("Masukkan kegiatan baru: ")
        kegiatan.append(kegiatan_baru)
        print(f"'{kegiatan_baru}' berhasil ditambahkan!")

    elif pilihan == '2':
        # Blok untuk menampilkan semua kegiatan (BELUM JADI)
        print("\n--- Daftar Kegiatan Anda ---")
        pass # Perintah ini belum melakukan apa-apa

    elif pilihan == '3':
        # Blok untuk menghapus kegiatan (ADA BUG)
        kegiatan_hapus = input("Masukkan kegiatan yang ingin dihapus: ")
        kegiatan.remove(kegiatan_hapus)
        print(f"'{kegiatan_hapus}' berhasil dihapus!")

    elif pilihan == '4':
        # Blok untuk keluar dari program (BELUM JADI)
        print("Terima kasih telah menggunakan aplikasi ini!")
        
    else:
        # Blok jika pengguna memasukkan pilihan yang tidak valid
        print("Pilihan tidak valid, silakan coba lagi.")
```
