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
# 1. CLASS (Blueprint Karakter)
class Karakter:
    # Method __init__ dijalankan secara otomatis saat objek baru dibuat
    def __init__(self, nama, kekuatan, health):
        # 3. ATTRIBUTE (Data yang dimiliki setiap karakter)
        self.nama = nama
        self.kekuatan = kekuatan
        self.health = health
        print(f"Karakter '{self.nama}' telah diciptakan!")

    # 4. METHOD (Perilaku yang bisa dilakukan karakter)
    def serang(self, musuh):
        """Metode untuk menyerang karakter lain."""
        print(f"{self.nama} menyerang {musuh.nama} dengan kekuatan {self.kekuatan}!")
        musuh.health -= self.kekuatan

    def tunjukkan_status(self):
        """Metode untuk menampilkan status health saat ini."""
        print(f"Status {self.nama}: Health = {self.health}")


# 2. OBJECT (Membuat karakter nyata dari blueprint)
print("--- Membuat Karakter ---")
ksatria = Karakter(nama="Aragon", kekuatan=25, health=100)
penyihir = Karakter(nama="Gandalf", kekuatan=35, health=80)
print("-" * 25)

# --- Simulasi Pertarungan ---
print("\n--- Pertarungan Dimulai! ---")
ksatria.tunjukkan_status()
penyihir.tunjukkan_status()

print("\nPenyihir menyerang Ksatria...")
penyihir.serang(ksatria) # Objek 'penyihir' menggunakan method 'serang' ke objek 'ksatria'

print("\nStatus setelah serangan:")
ksatria.tunjukkan_status()
penyihir.tunjukkan_status()
```
