# ✨ 23: Parameter Fleksibel (\*args dan \*\*kwargs)

Bagaimana jika kita ingin membuat fungsi yang bisa menerima jumlah parameter yang tidak menentu? Misalnya, fungsi untuk menjumlahkan 2 angka, 5 angka, atau bahkan 100 angka. Inilah gunanya `*args` dan `**kwargs`.

### `*args` (untuk Argumen Posisi)

`*args` akan mengumpulkan semua argumen posisi yang diberikan ke dalam sebuah **tuple**. Nama `args` adalah konvensi, yang penting adalah tanda bintang `*`.

```python
def jumlahkan_semua(*daftar_angka):
    print(f"Data yang masuk (berupa tuple): {daftar_angka}")
    total = 0
    for angka in daftar_angka:
        total += angka
    return total

# Memanggil dengan jumlah argumen berbeda
print(jumlahkan_semua(1, 2))
print(jumlahkan_semua(10, 20, 30, 40))
```
