# 🏛️ 19: Tipe Data Tuple

**Tuple** sangat mirip dengan List, tapi dengan satu perbedaan kunci: Tuple **tidak bisa diubah (immutable)**. Sekali dibuat, isinya tidak bisa ditambah, diubah, atau dihapus.

### Kapan Menggunakan Tuple?

Gunakan tuple untuk data yang seharusnya tidak pernah berubah, seperti:

- Koordinat (x, y)
- Kode warna RGB (Red, Green, Blue)
- Data konfigurasi yang bersifat tetap

### Perbedaan Utama

```python
# List (Mutable)
list_saya = [1, 2, 3]
list_saya[0] = 100 # BISA
print(f"List: {list_saya}")

# Tuple (Immutable)
tuple_saya = (1, 2, 3)
# tuple_saya[0] = 100 # AKAN ERROR! TypeError
print(f"Tuple: {tuple_saya}")
```
