# ⚖️ 09: Operator Perbandingan

Operator ini digunakan untuk membandingkan dua nilai. Hasilnya SELALU `True` atau `False`.

### Konsep Kunci

| Operator | Arti                       | Contoh   | Hasil   |
| :------- | :------------------------- | :------- | :------ |
| `==`     | Sama dengan                | `5 == 5` | `True`  |
| `!=`     | Tidak sama dengan          | `5 != 5` | `False` |
| `>`      | Lebih besar dari           | `5 > 3`  | `True`  |
| `<`      | Lebih kecil dari           | `5 < 3`  | `False` |
| `>=`     | Lebih besar dari atau sama | `5 >= 5` | `True`  |
| `<=`     | Lebih kecil dari atau sama | `5 <= 3` | `False` |

**Penting:** `==` (membandingkan) sangat berbeda dengan `=` (memberi nilai)!

### 💻 Proyek: "Pengecek Usia SIM"

Program ini akan menghasilkan nilai `True` atau `False` berdasarkan perbandingan usia.

**Buat File `cek_usia.py` dan Salin Kode:**

```python
usia_pemohon = 18
usia_minimal_sim = 17

# Lakukan perbandingan dan simpan hasilnya di variabel boolean
apakah_cukup_umur = usia_pemohon >= usia_minimal_sim

print(f"Usia pemohon: {usia_pemohon} tahun")
print(f"Syarat usia minimal: {usia_minimal_sim} tahun")
print(f"Apakah pemohon sudah cukup umur? {apakah_cukup_umur}")

# Kode ini adalah 'preview' untuk topik berikutnya (If-Else)
if apakah_cukup_umur:
    print("Status: Boleh membuat SIM.")
else:
    print("Status: Belum boleh membuat SIM.")
```
