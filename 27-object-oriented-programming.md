# 🏗️ 27: Pemrograman Berorientasi Objek (OOP)

**OOP** adalah sebuah cara pandang dalam menulis kode, di mana kita mengorganisir program kita seperti dunia nyata: penuh dengan **objek** yang memiliki **data (properti)** dan **perilaku (aksi)**.

### Konsep Inti OOP

#### 1. Class (Cetak Biru / Blueprint)

**Class** adalah rancangan atau cetak biru untuk membuat objek. Misalnya, `class Mobil` adalah cetak biru yang menjelaskan bahwa semua mobil pasti punya warna, merk, dan bisa berjalan.

#### 2. Object (Objek Nyata / Instance)

**Object** adalah hasil nyata yang dibuat dari sebuah Class. Misalnya, `mobil_budi` (berwarna merah, merk Toyota) dan `mobil_ani` (berwarna hitam, merk Honda) adalah dua objek berbeda yang dibuat dari `class Mobil` yang sama.

#### 3. Attribute (Properti)

**Attribute** adalah data yang dimiliki oleh sebuah objek. Didefinisikan di dalam method khusus bernama `__init__`. Misalnya, `warna` dan `merk` adalah atribut dari objek mobil.

#### 4. Method (Perilaku)

**Method** adalah fungsi yang ada di dalam sebuah class. Ini mendefinisikan apa yang bisa dilakukan oleh objek tersebut. Misalnya, `maju()` atau `klakson()` adalah method dari objek mobil.

### 💻 Proyek Sederhana: "Database Karakter Game"

Kita akan membuat `class` untuk karakter di sebuah game.

**A. Buat File `game_karakter.py` dan Salin Kode:**

```python
# 1. CLASS (Blueprint Mobil)
class Mobil:
    # Method __init__ dijalankan saat objek mobil baru dibuat
    def __init__(self, merek, kecepatan, bahan_bakar):
        # 3. ATTRIBUTE (Data yang dimiliki setiap mobil)
        self.merek = merek
        self.kecepatan = kecepatan
        self.bahan_bakar = bahan_bakar
        print(f"Mobil '{self.merek}' telah dibuat!")

    # 4. METHOD (Perilaku mobil)
    def berjalan(self, jarak):
        """Metode untuk membuat mobil berjalan sejauh jarak tertentu."""
        print(f"{self.merek} berjalan sejauh {jarak} km dengan kecepatan {self.kecepatan} km/jam.")
        # Setiap 10 km menghabiskan 1 liter bahan bakar
        penggunaan_bbm = jarak / 10
        self.bahan_bakar -= penggunaan_bbm
        if self.bahan_bakar < 0:
            self.bahan_bakar = 0
        print(f"Bahan bakar tersisa: {self.bahan_bakar:.1f} liter")

    def isi_bensin(self, liter):
        """Metode untuk menambah bahan bakar."""
        self.bahan_bakar += liter
        print(f"{self.merek} telah diisi bensin sebanyak {liter} liter. Total sekarang: {self.bahan_bakar:.1f} liter")

    def tampilkan_status(self):
        """Menampilkan status mobil saat ini."""
        print(f"Status {self.merek}: Kecepatan = {self.kecepatan} km/jam, Bahan Bakar = {self.bahan_bakar:.1f} liter")


# 2. OBJECT (Membuat mobil nyata dari blueprint)
print("--- Membuat Mobil ---")
mobil_sport = Mobil(merek="Ferrari", kecepatan=220, bahan_bakar=50)
mobil_keluarga = Mobil(merek="Toyota Avanza", kecepatan=120, bahan_bakar=60)
print("-" * 30)

# --- Simulasi Perjalanan ---
print("\n--- Perjalanan Dimulai! ---")
mobil_sport.tampilkan_status()
mobil_keluarga.tampilkan_status()

print("\nFerrari berjalan sejauh 120 km...")
mobil_sport.berjalan(120)

print("\nToyota Avanza berjalan sejauh 80 km...")
mobil_keluarga.berjalan(80)

print("\nStatus setelah perjalanan:")
mobil_sport.tampilkan_status()
mobil_keluarga.tampilkan_status()

print("\nMengisi bensin Ferrari sebanyak 20 liter...")
mobil_sport.isi_bensin(20)

print("\nStatus akhir:")
mobil_sport.tampilkan_status()
mobil_keluarga.tampilkan_status()

```
