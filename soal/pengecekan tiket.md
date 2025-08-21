# Proyek Sederhana - Pengecekan Wahana Petualangan 🎢

Selamat datang di proyek "Pengecekan Wahana Petualangan"! Ini adalah program sederhana untuk mensimulasikan proses pengecekan tiket di sebuah taman hiburan. Program ini dirancang untuk menunjukkan bagaimana kita bisa membuat keputusan yang kompleks di dalam kode menggunakan logika dasar Python.

```python
print("--- Sistem Pengecekan Wahana Petualangan ---")

usia = int(input("Masukan usia anda                : "))
tinggi_badan = int(input("Masukan tinggi badan anda (cm) :")) # dalam cm
punya_tiket_vip = False

if punya_tiket_vip or (tinggi_badan >= 120 and tinggi_badan <= 200):

    print("✅ Syarat tinggi badan terpenuhi atau Anda pemegang tiket VIP. Silakan lanjut.")

    # LEVEL 2: Kondisi Bersarang (Nested If) untuk menentukan harga tiket
    # Pengecekan harga ini HANYA terjadi jika syarat pertama sudah lolos.
    if usia < 12:
        harga_tiket = "Rp 25.000 (Anak-anak)"
    else:
        harga_tiket = "Rp 40.000 (Dewasa)"

    print(f"Harga tiket Anda: {harga_tiket}")

elif tinggi_badan < 120:
    print("❌ Maaf, tinggi badan Anda tidak mencukupi untuk wahana ini.")
else:
    print("❌ Maaf, tinggi badan Anda melebihi batas maksimal wahana ini.")

print("\n--- Pengecekan Selesai ---")
```
