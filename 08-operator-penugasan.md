# ⚡ 08: Operator Penugasan

Operator penugasan adalah cara singkat (`shortcut`) untuk melakukan operasi matematika dan menyimpan hasilnya kembali ke variabel yang sama.

### Konsep Kunci

Operator dasar adalah `=`. Operator lainnya adalah jalan pintas:

| Shortcut | Sama Dengan... |
| :------- | :------------- |
| `x += 5` | `x = x + 5`    |
| `x -= 5` | `x = x - 5`    |
| `x *= 5` | `x = x * 5`    |
| `x /= 5` | `x = x / 5`    |

### 💻 Proyek: "Simulasi Poin Game"

**A. Buat File `game_poin.py` dan Salin Kode:**

```python
poin = 100
print(f"Poin awal pemain: {poin}")

# Pemain mengalahkan musuh, dapat 20 poin
poin += 20
print(f"Mengalahkan musuh! Poin sekarang: {poin}")

# Pemain terkena jebakan, kehilangan 10 poin
poin -= 10
print(f"Terkena jebakan! Poin sekarang: {poin}")

# Poin digandakan karena item langka
poin *= 2
print(f"Dapat item langka! Poin digandakan menjadi: {poin}")
```
