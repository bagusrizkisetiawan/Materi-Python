# 🧠 13: Operator Logika (and, or, not)

Operator logika adalah "lem" yang menggabungkan beberapa kondisi `True`/`False` menjadi satu kesimpulan akhir.

### Konsep Kunci

#### `and` (dan)

Hasilnya `True` hanya jika **SEMUA** kondisi bernilai `True`.

| Kondisi 1 | Operator | Kondisi 2 | Hasil   |
| :-------- | :------: | :-------- | :------ |
| `True`    |  `and`   | `True`    | `True`  |
| `True`    |  `and`   | `False`   | `False` |
| `False`   |  `and`   | `True`    | `False` |
| `False`   |  `and`   | `False`   | `False` |

#### `or` (atau)

Hasilnya `True` jika **SALAH SATU** kondisi saja sudah bernilai `True`.

| Kondisi 1 | Operator | Kondisi 2 | Hasil   |
| :-------- | :------: | :-------- | :------ |
| `True`    |   `or`   | `True`    | `True`  |
| `True`    |   `or`   | `False`   | `True`  |
| `False`   |   `or`   | `True`    | `True`  |
| `False`   |   `or`   | `False`   | `False` |

#### `not` (bukan/negasi)

Membalik nilai boolean: `not True` menjadi `False`, dan `not False` menjadi `True`.

### 💻 Proyek: "Pengecek Syarat Pendaftaran"

Program untuk memeriksa apakah seorang calon siswa boleh mendaftar kursus.
Syarat: Lulusan SMA **DAN** usianya di bawah 25 tahun.

**A. Buat File `cek_pendaftaran.py` dan Salin Kode:**

```python
status_pendidikan = "SMA"
usia = 22

# Menggabungkan dua kondisi dengan 'and'
apakah_memenuhi_syarat = (status_pendidikan == "SMA") and (usia < 25)

print(f"Status Pendidikan: {status_pendidikan}")
print(f"Usia: {usia}")
print("--- Mengecek Syarat ---")
print(f"Apakah calon siswa memenuhi syarat? {apakah_memenuhi_syarat}")
```
