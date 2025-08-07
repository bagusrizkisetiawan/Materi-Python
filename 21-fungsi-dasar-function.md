# 📦 21: Fungsi Dasar (Function)

**Fungsi** adalah blok kode yang terorganisir, diberi nama, dan dapat digunakan kembali untuk melakukan tugas tertentu. Anggap saja seperti resep masakan: Anda memberinya bahan (parameter), ia akan memprosesnya, dan mengembalikan hasil masakan (return value).

### Kenapa Kita Butuh Fungsi?

Untuk menerapkan prinsip **DRY (Don't Repeat Yourself)**. Bayangkan Anda perlu menghitung luas persegi panjang di banyak tempat.

**Tanpa Fungsi (Boros Kode):**

```python
# Hitung luas 1
panjang1 = 10
lebar1 = 5
luas1 = panjang1 * lebar1
print(luas1)

# Hitung luas 2
panjang2 = 7
lebar2 = 3
luas2 = panjang2 * lebar2
print(luas2)
```

**Dengan function (efisien):**

```python
def hitung_luas_persegi(panjang, lebar):
    return panjang * lebar

luas1 = hitung_luas_persegi(10, 5)
luas2 = hitung_luas_persegi(7, 3)
print(luas1)
print(luas2)
```

**Anatomi function**

```python
def nama_fungsi(parameter1, parameter2):
    """Docstring: Penjelasan singkat tentang fungsi ini."""
    # Blok kode yang akan dieksekusi
    proses = parameter1 + parameter2
    return proses # Mengembalikan hasil
```
