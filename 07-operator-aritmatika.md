# 🧮 07: Operator Aritmatika

Operator aritmatika adalah simbol yang kita gunakan untuk melakukan perhitungan matematika.

### Konsep Kunci

| Operator | Nama               | Contoh   | Hasil |
| :------- | :----------------- | :------- | :---- |
| `+`      | Penjumlahan        | `5 + 2`  | `7`   |
| `-`      | Pengurangan        | `5 - 2`  | `3`   |
| `*`      | Perkalian          | `5 * 2`  | `10`  |
| `/`      | Pembagian          | `5 / 2`  | `2.5` |
| `%`      | Modulo (Sisa Bagi) | `5 % 2`  | `1`   |
| `**`     | Pangkat (Eksponen) | `5 ** 2` | `25`  |
| `//`     | Pembagian Bulat    | `5 // 2` | `2`   |

### 💡 Level Up: Urutan Operasi

Python mengikuti aturan **PEMDAS/BODMAS** (kurung, pangkat, kali/bagi, tambah/kurang). `2 + 3 * 4` hasilnya `14`, bukan `20`.

### 💻 Proyek: "Kalkulator Luas Bangun Datar"

**A. Buat File `kalkulator_luas.py` dan Salin Kode:**

```python
# Menghitung Luas Persegi Panjang
panjang = 10
lebar = 5
luas_persegi_panjang = panjang * lebar
print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas_persegi_panjang}")

# Menghitung Luas Segitiga
alas = 8
tinggi = 6
luas_segitiga = 0.5 * alas * tinggi # atau (alas * tinggi) / 2
print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas_segitiga}")
```
