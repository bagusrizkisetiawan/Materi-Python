# 🛡️ 25: Penanganan Error (Try-Except)

Saat program berjalan, kadang terjadi error yang tidak terduga (misalnya pengguna salah input). Jika tidak ditangani, error ini akan membuat program berhenti total atau **crash**.

`try-except` adalah cara kita membuat "jaring pengaman". Kita menyuruh Python: "**Coba (try)** lakukan ini. Jika gagal dan terjadi error, **kecuali (except)** jangan panik, tapi lakukan itu sebagai gantinya."

### Anatomi `try-except`

```python
try:
    # Blok kode yang berpotensi menimbulkan error
    angka = int(input("Masukkan sebuah angka: "))
    hasil = 10 / angka
    print(f"Hasilnya adalah {hasil}")
except ValueError:
    # Blok ini hanya berjalan jika terjadi error konversi tipe data
    print("Error: Input yang Anda masukkan bukan angka!")
except ZeroDivisionError:
    # Blok ini hanya berjalan jika terjadi error pembagian dengan nol
    print("Error: Angka tidak boleh dibagi dengan nol!")
except Exception as e:
    # Menangkap semua jenis error lain yang mungkin terjadi
    print(f"Terjadi error tak terduga: {e}")
```

### 💻 Proyek Sederhana: "Kalkulator Anti-Error"

Membuat program pembagian sederhana yang tidak akan crash meskipun pengguna salah memasukkan input.

**Buat File kalkulator_aman.py dan Salin Kode:**

```python
print("--- Program Pembagian Aman ---")

try:
    # Mencoba mendapatkan input dan mengubahnya menjadi angka
    pembilang = float(input("Masukkan angka yang ingin dibagi: "))
    penyebut = float(input("Masukkan angka pembagi: "))

    # Mencoba melakukan operasi pembagian
    hasil = pembilang / penyebut

    # Jika semua berhasil, tampilkan hasilnya
    print(f"Hasil dari {pembilang} / {penyebut} adalah {hasil}")

except ValueError:
    # Jika input tidak bisa diubah menjadi angka (misal: "abc")
    print("Oops! Input harus berupa angka. Program dihentikan.")
except ZeroDivisionError:
    # Jika pengguna mencoba membagi dengan nol
    print("Oops! Angka tidak bisa dibagi dengan nol. Program dihentikan.")
```
