# 🎯 24: Tipe Data Set (Himpunan)

**Set** adalah tipe data koleksi yang mirip seperti `List`, namun memiliki dua sifat unik yang sangat penting:

1.  **Tidak Ada Duplikat**: Set secara otomatis membuang semua elemen yang sama.
2.  **Tidak Terurut (Unordered)**: Elemen di dalam set tidak memiliki urutan indeks yang pasti. Anda tidak bisa mengambil elemen dengan `my_set[0]`.

Anggap saja `Set` seperti lingkaran pertemanan: setiap orang di dalamnya unik dan tidak ada urutan senioritas.

### Operasi Himpunan

Kekuatan utama Set ada pada operasinya, sama seperti himpunan di matematika.

```python
hobi_budi = {"membaca", "berenang", "bermain game"}
hobi_citra = {"memasak", "berenang", "melukis"}

# Union (|): Gabungan semua hobi unik dari keduanya
hobi_bersama = hobi_budi | hobi_citra

# Intersection (&): Hobi yang sama-sama mereka miliki
hobi_yang_sama = hobi_budi & hobi_citra

# Difference (-): Hobi yang dimiliki Budi tapi tidak dimiliki Citra
hobi_unik_budi = hobi_budi - hobi_citra
```

### 💻 Proyek Sederhana: "Analisis Hobi Kelompok"

Program untuk menemukan hobi yang sama dan hobi yang berbeda dari dua orang.

**Buat File analisis_hobi.py dan Salin Kode:**

```python
# Data hobi dua orang
hobi_andi = {"futsal", "nonton film", "main gitar", "mendaki"}
hobi_bella = {"memasak", "nonton film", "berkebun", "main gitar"}

print(f"Hobi Andi: {hobi_andi}")
print(f"Hobi Bella: {hobi_bella}")
print("-" * 30)

# 1. Menemukan hobi yang sama (Intersection)
hobi_sama = hobi_andi.intersection(hobi_bella)
print(f"Hobi yang mereka sukai bersama: {hobi_sama}")

# 2. Menemukan semua hobi unik gabungan (Union)
semua_hobi = hobi_andi.union(hobi_bella)
print(f"Semua hobi jika digabungkan: {semua_hobi}")

# 3. Menemukan hobi yang hanya dimiliki Andi (Difference)
hobi_hanya_andi = hobi_andi.difference(hobi_bella)
print(f"Hobi yang hanya dimiliki Andi: {hobi_hanya_andi}")
```
