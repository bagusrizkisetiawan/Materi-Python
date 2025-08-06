# 🛒 17: Tipe Data List

**List** adalah kumpulan data yang terurut dan **bisa diubah (mutable)**. Anggap saja seperti daftar belanja yang bisa kamu tambah, coret, atau ganti isinya.

### Operasi Dasar (CRUD)

- **Create (Membuat)**: `tugas_harian = ["Belajar Python", "Mengerjakan PR"]`
- **Read (Membaca)**: Mengakses berdasarkan urutan (indeks), dimulai dari 0. `tugas_harian[0]` hasilnya `"Belajar Python"`.
- **Update (Memperbarui)**: `tugas_harian[1] = "Olahraga Sore"`
- **Delete (Menghapus)**: `.remove("Belajar Python")` atau `del tugas_harian[0]`

### 💻 Proyek: "To-Do List Manager"

**Buat File `todo_list.py` dan Salin Kode:**

```python
# --- Memahami Konsep List (Versi Sederhana) ---

# 1. CREATE: Membuat sebuah list (daftar tugas) dengan beberapa item awal.
print("--- 1. Membuat List ---")
daftar_tugas = ["Belajar Python Dasar", "Sarapan Pagi", "Mengerjakan PR"]
print(f"Isi list awalku: {daftar_tugas}")
print("\n") # Memberi spasi agar rapi

# ----------------------------------------------------------------

# 2. READ: Membaca atau mengakses isi list.
print("--- 2. Membaca Isi List ---")

# Membaca item pertama (ingat, indeks/urutan di Python dimulai dari 0)
tugas_pertama = daftar_tugas[0]
print(f"Tugas pertamaku adalah: '{tugas_pertama}'")

# Mengetahui ada berapa banyak item di dalam list
jumlah_tugas = len(daftar_tugas)
print(f"Saat ini, total ada {jumlah_tugas} tugas dalam daftar.")
print("\n")

# ----------------------------------------------------------------

# 3. UPDATE: Mengubah item yang sudah ada di dalam list.
print("--- 3. Mengubah Item di List ---")
print(f"List sebelum diubah: {daftar_tugas}")

# Kita ubah item kedua (indeks ke-1) dari "Sarapan Pagi" menjadi "Olahraga Pagi"
daftar_tugas[1] = "Olahraga Pagi"
print(f"List setelah diubah: {daftar_tugas}")
print("\n")

# ----------------------------------------------------------------

# 4. ADD (Tambah): Menambahkan item baru ke *akhir* list menggunakan .append()
print("--- 4. Menambah Item Baru ---")
print(f"List sebelum ditambah: {daftar_tugas}")
daftar_tugas.append("Membaca Buku")
print(f"List setelah ditambah item baru: {daftar_tugas}")
print("\n")

# ----------------------------------------------------------------

# 5. DELETE: Menghapus item dari list.
print("--- 5. Menghapus Item dari List ---")
print(f"List sebelum dihapus: {daftar_tugas}")

# Cara pertama: Menghapus berdasarkan isi/namanya menggunakan .remove()
# Kita hapus tugas 'Mengerjakan PR'
daftar_tugas.remove("Mengerjakan PR")
print(f"List setelah 'Mengerjakan PR' dihapus: {daftar_tugas}")

# Cara kedua: Menghapus berdasarkan urutan/indeksnya menggunakan 'del'
# Kita hapus item pertama (indeks 0) yang sekarang adalah 'Belajar Python Dasar'
del daftar_tugas[0]
print(f"List setelah item pertama dihapus: {daftar_tugas}")
print("\n")

# ----------------------------------------------------------------

print("--- SELESAI ---")
print(f"Setelah semua proses, sisa tugasku sekarang adalah: {daftar_tugas}")
```
