# 🍰 12: Kondisi Bersarang (Nested If)

_Nested If_ adalah sebuah pernyataan `if` yang berada di dalam blok `if` atau `else` lain. Ini seperti kue lapis, ada pengecekan di dalam pengecekan.

### Kapan Digunakan?

Saat sebuah syarat hanya perlu diperiksa jika syarat sebelumnya sudah terpenuhi.

### 💻 Proyek: "Pendaftaran Anggota Premium"

Syarat: Pengguna harus berusia di atas 18 TAHUN, **DAN** saldonya harus cukup.

**Buat File `daftar_premium.py` dan Salin Kode:**

```python
usia = 25
saldo = 500000
biaya_premium = 250000

print("--- Proses Pendaftaran Anggota Premium ---")

# Pengecekan tingkat pertama: Usia
if usia >= 18:
    print("✅ Syarat usia terpenuhi.")

    # Pengecekan tingkat kedua (bersarang): Saldo
    # Ini hanya akan diperiksa jika syarat usia sudah lolos.
    if saldo >= biaya_premium:
        print("✅ Syarat saldo terpenuhi.")
        print("🎉 Selamat! Anda berhasil mendaftar sebagai anggota premium.")
    else:
        print("❌ Syarat saldo tidak terpenuhi.")
        print("Maaf, saldo Anda tidak cukup untuk mendaftar.")

else:
    print("❌ Syarat usia tidak terpenuhi.")
    print("Maaf, Anda harus berusia minimal 18 tahun untuk mendaftar.")
```
