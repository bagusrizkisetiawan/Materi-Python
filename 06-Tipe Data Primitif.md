# 📊 06: Tipe Data Primitif

Setiap data dalam Python memiliki "jenis" atau **tipe data**. Ini penting agar Python tahu cara mengolah data tersebut. Tipe data dasar (primitif) adalah pondasi dari semua data yang lebih kompleks.

### Konsep Kunci

- **Integer (`int`)**: Bilangan bulat (tanpa desimal). Contoh: `10`, `-50`, `2025`.
- **Float (`float`)**: Bilangan desimal (menggunakan titik). Contoh: `3.14`, `99.9`, `0.5`.
- **String (`str`)**: Kumpulan karakter atau teks (diapit `"` atau `'`). Contoh: `"Halo Purwokerto"`, `'Python'`.
- **Boolean (`bool`)**: Nilai logika kebenaran. Hanya ada dua: `True` atau `False`.

### 💻 Proyek: "Kalkulator Sederhana"

Mari kita gunakan tipe data `int` dan `float` untuk membuat kalkulator.

**A. Buat File `kalkulator_dasar.py` dan Salin Kode:**

```python
# Variabel angka1 dan angka2 adalah tipe data Integer (int)
angka1 = 10
angka2 = 5

print(f"--- Kalkulator Sederhana ---")
print(f"Angka pertama: {angka1}")
print(f"Angka kedua: {angka2}")
print("----------------------------")

# Operasi akan menghasilkan int atau float
penjumlahan = angka1 + angka2
pengurangan = angka1 - angka2
perkalian = angka1 * angka2
pembagian = angka1 / angka2 # Pembagian selalu menghasilkan float!

print(f"Hasil Penjumlahan: {penjumlahan} (Tipe: {type(penjumlahan)})")
print(f"Hasil Pengurangan: {pengurangan} (Tipe: {type(pengurangan)})")
print(f"Hasil Perkalian: {perkalian} (Tipe: {type(perkalian)})")
print(f"Hasil Pembagian: {pembagian} (Tipe: {type(pembagian)})")
```
