# 🛣️ 10: Kondisi If-Else

Struktur `if-else` adalah seperti persimpangan jalan bagi program. Jika suatu kondisi benar (`True`), program akan mengambil satu jalur. Jika salah (`False`), ia akan mengambil jalur lain.

### Sintaks Dasar

```python
if kondisi:
    # Blok kode ini dijalankan JIKA kondisi True
    # Perhatikan indentasi (jarak dari kiri)!
else:
    # Blok kode ini dijalankan JIKA kondisi False
```

### 💻 Proyek: "Pengecek Kata Sandi"

**A. Buat File login.py dan Salin Kode:**

```python
kata_sandi_benar = "purwokerto_keren"
kata_sandi_input = input("Masukkan kata sandi Anda: ") # Minta input dari pengguna

if kata_sandi_input == kata_sandi_benar:
    print("Akses Diterima! Selamat datang kembali.")
else:
    print("Akses Ditolak! Kata sandi yang Anda masukkan salah.")

print("--- Program Selesai ---")
```

**B. Jalankan Program**

Coba jalankan dua kali: sekali dengan kata sandi yang benar, dan sekali lagi dengan yang salah untuk melihat kedua jalur bekerja.
