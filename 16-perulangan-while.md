# ⏳ 16: Perulangan (While Loop)

`while loop` terus berjalan **selama** kondisinya bernilai `True`. Ini cocok untuk perulangan yang jumlahnya tidak pasti.

### Struktur Dasar

```python
# 1. Inisialisasi
counter = 0

# 2. Kondisi
while counter < 5:
    print(f"Perulangan ke-{counter}")
    # 3. Update (PENTING! Agar tidak infinite loop)
    counter += 1
```

### 💻 Proyek: "Menu Aplikasi Sederhana"

**Buat File menu_app.py dan Salin Kode:**

```python
while True: # Loop ini akan berjalan selamanya sampai ada 'break'
    print("\n--- APLIKASI KASIR ---")
    print("1. Tambah Barang")
    print("2. Lihat Total Belanja")
    print("3. Bayar")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan Anda (1-4): ")

    if pilihan == '1':
        print("Anda memilih Tambah Barang.")
    elif pilihan == '2':
        print("Anda memilih Lihat Total Belanja.")
    elif pilihan == '3':
        print("Anda memilih Bayar.")
    elif pilihan == '4':
        print("Terima kasih! Keluar dari program.")
        break # Perintah untuk menghentikan loop
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
```
