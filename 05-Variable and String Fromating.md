# 🚀 Variabel dan Format String

Selamat datang di sesi belajar Python! Di sini, kita akan mengupas tuntas cara membuat biodata yang dinamis. Kamu akan belajar bagaimana cara menyimpan informasi dalam "wadah" yang disebut **variabel** dan menampilkannya dengan rapi menggunakan teknik **Format String**.

Siap? Mari kita mulai!

---

### 🤔 Langkah 1: Memahami Konsep

Sebelum coding, kita pahami dulu dua konsep kuncinya:

1.  **Variabel**: Bayangkan kamu punya beberapa kotak. Setiap kotak kamu beri label (misalnya `nama`, `umur`, `kota`). Di dalam setiap kotak, kamu bisa menyimpan satu informasi. Kotak berlabel inilah yang kita sebut **variabel**.

    ```python
    # Contoh:
    nama = "Citra"  # Variabel 'nama' berisi teks "Citra"
    umur = 22       # Variabel 'umur' berisi angka 22
    ```

2.  **Format String (f-string)**: Ini adalah cara ajaib untuk menyusun kalimat dengan mengambil isi dari variabel-variabelmu. Kamu tinggal tulis huruf `f` sebelum tanda kutip, lalu sebut nama variabel di dalam kurung kurawal `{}`.

    ```python
    # Tanpa f-string (kurang praktis)
    # print("Nama saya " + nama + " dan umur saya " + str(umur))

    # Dengan f-string (bersih dan mudah dibaca!)
    print(f"Nama saya {nama} dan umur saya {umur}")
    ```
