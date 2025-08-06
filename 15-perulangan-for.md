# 🤖 15: Perulangan (For Loop)

Bayangkan Anda harus menulis "Selamat Pagi!" sebanyak 100 kali. Menulis `print()` 100 kali tentu sangat melelahkan. Di sinilah **perulangan (loop)** berperan. Perulangan adalah cara untuk menyuruh komputer melakukan tugas yang sama berulang-ulang secara otomatis.

`for loop` adalah jenis perulangan yang paling umum, digunakan untuk "mengunjungi" setiap item dalam sebuah urutan data.

### Kenapa Kita Butuh Perulangan?

Lihat perbandingan ini. Misalkan kita ingin mencetak angka 1 sampai 5.

**Cara Manual (Tidak Efisien):**

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

### Cara dengan for loop (Efisien dan Ringkas):

```python
for angka in range(1, 6):
    print(angka)
```

`for loop` digunakan untuk melakukan tugas berulang sebanyak jumlah yang sudah ditentukan. Sangat cocok digunakan dengan fungsi `range()`.

### Konsep `range()`

- `range(5)`: Menghasilkan urutan angka dari 0, 1, 2, 3, 4. (5 angka)

- `range(1, 6)`: Menghasilkan urutan dari 1, 2, 3, 4, 5. (Mulai dari 1, berhenti sebelum 6)

- `range(0, 10, 2)`: Menghasilkan urutan 0, 2, 4, 6, 8. (Lompat 2 setiap kali)

<br>

### 💻 Proyek: "Guessing Number Game" (dengan kesempatan terbatas)

**A. Buat File `tebak_angka_for.py` dan Salin Kode:**

```python
import random

# 1. PERSIAPAN GAME
# Komputer memilih angka acak antara 1 dan 10 (kita persempit jangkauannya agar lebih mudah)
angka_rahasia = random.randint(1, 10)
jumlah_kesempatan = 3

# Variabel ini kita sebut "flag" atau penanda. Awalnya kita anggap pemain belum menang.
pemain_menang = False

print("--- Selamat Datang di Game Tebak Angka! ---")
print(f"Aku punya angka rahasia antara 1 sampai 10.")
print(f"Kamu punya {jumlah_kesempatan} kesempatan untuk menebak.")


# 2. MEMULAI PERULANGAN
# Kita akan mengulang proses tebakan sebanyak 'jumlah_kesempatan'
for kesempatan_ke in range(jumlah_kesempatan):
    print(f"\n--- Kesempatan ke-{kesempatan_ke + 1} ---")

    # Minta input dari pemain dan langsung ubah menjadi angka (integer)
    tebakan_pemain = int(input("Masukkan tebakanmu: "))

    # 3. LOGIKA PENGECEKAN
    # Cek apakah tebakan pemain sama dengan angka rahasia
    if tebakan_pemain == angka_rahasia:
        print(f"🎉 Selamat! Kamu benar! Angkanya adalah {angka_rahasia}.")
        pemain_menang = True  # Ubah penanda karena pemain sudah menang
        break  # Hentikan perulangan karena game sudah selesai

    # Jika tebakan salah, beri petunjuk
    elif tebakan_pemain < angka_rahasia:
        print("Angkamu terlalu rendah! Coba lagi.")
    else:
        print("Angkamu terlalu tinggi! Coba lagi.")


# 4. KESIMPULAN GAME (SETELAH LOOP SELESAI)
# Setelah perulangan selesai, kita cek variabel penanda.
# Jika pemain TIDAK menang (nilainya masih False), berarti kesempatannya habis.
if not pemain_menang:
    print(f"\nGame Over! Kesempatanmu habis.")
    print(f"Angka rahasia yang benar adalah {angka_rahasia}.")
```
