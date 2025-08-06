# 📖 20: Tipe Data Dictionary

**Dictionary** adalah kumpulan data yang disimpan dalam format **`kunci:nilai` (`key:value`)**. Ini seperti kamus sungguhan: kamu mencari kata (kunci) untuk menemukan artinya (nilai).

### Karakteristik Utama

- **Tidak diakses dengan indeks angka**, melainkan dengan `key` yang unik.
- **Sangat cepat** untuk menemukan data berdasarkan kuncinya.
- **Bisa diubah (mutable)**.

### Operasi Dasar

```python
# Membuat Dictionary
biodata = {
    "nama": "Budi",
    "kota": "Purwokerto",
    "umur": 25
}

# Membaca data
print(f"Nama: {biodata['nama']}")

# Menambah / Mengubah data
biodata['pekerjaan'] = "Programmer" # Menambah data baru
biodata['kota'] = "Jakarta"      # Mengubah data yang sudah ada

# Menghapus data
del biodata['umur']

print(biodata)
```

### 💻 Proyek: "Book Inventory System"

**Buat File inventaris_buku.py dan Salin Kode:**

```python
# Kunci adalah kode buku (unik), Nilai adalah judul buku
inventaris = {
    "b-123": "The Great Gatsby",
    "b-122": "1984",
    "b-132": "To Kill a Mockingbird"
}

# Menambah buku baru
inventaris["b-322"] = "The Catcher in the Rye"

# Mencari buku berdasarkan ISBN
kode_buku = "b-122"
if kode_buku in inventaris:
    print(f"Buku dengan kode:  {kode_buku} ditemukan: {inventaris[kode_buku]}")
else:
    print("Buku tidak ditemukan.")

# Menampilkan semua buku dengan perulangan
print("\n--- Semua Buku di Inventaris ---")
for kode_buku, judul in inventaris.items():
    print(f"- kode_buku: {kode_buku}, Judul: {judul}")
```
