# 🚦 11: Kondisi If-Elif-Else

Bagaimana jika ada lebih dari dua pilihan, seperti di lampu lalu lintas (merah, kuning, hijau)? Kita gunakan `if-elif-else`. `elif` adalah singkatan dari "else if".

### Alur Logika

1.  Python cek kondisi `if`. Jika `True`, jalankan bloknya dan selesai.
2.  Jika `if` salah, Python cek kondisi `elif` pertama. Jika `True`, jalankan bloknya dan selesai.
3.  Proses berlanjut ke `elif` berikutnya jika ada.
4.  Jika semua `if` dan `elif` salah, blok `else` akan dijalankan.

### 💻 Proyek: "Pengklasifikasi Nilai"

**Buat File `cek_nilai.py` dan Salin Kode:**

```python
nilai_siswa = 85

print(f"Siswa mendapat nilai: {nilai_siswa}")

if nilai_siswa >= 85:
    predikat = "A (Istimewa)"
elif nilai_siswa >= 75:
    predikat = "B (Baik)"
elif nilai_siswa >= 65:
    predikat = "C (Cukup)"
elif nilai_siswa >= 50:
    predikat = "D (Kurang)"
else:
    predikat = "E (Gagal)"

print(f"Predikat yang didapat: {predikat}")
```
