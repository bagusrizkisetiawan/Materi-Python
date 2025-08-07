# 🖨️ 03: Output dan input (Fungsi Print dan input)

Konsep paling dasar dalam pemrograman adalah **Input -> Proses -> Output**.

- **Input**: Data yang kita berikan.
- **Proses**: Apa yang komputer lakukan pada data.
- **Output**: Hasil yang ditampilkan komputer.

Hari ini kita fokus pada **Output**. Perintah paling dasar untuk menampilkan output di Python adalah `print()`.

### Apa itu `print()`?

`print()` adalah sebuah **fungsi** bawaan Python yang tugasnya menampilkan apa pun yang kita letakkan di dalam tanda kurungnya ke layar.

```python
print("Halo, ini tulisan pertamaku!")
print(12345)
```

### Apa itu `input()`?

`input()` adalah fungsi untuk "berhenti sejenak" dan meminta pengguna mengetikkan sesuatu. Teks yang diketik oleh pengguna akan ditangkap oleh program untuk diproses lebih lanjut.

Penting: Apapun yang diketik pengguna, `input()` akan selalu menganggapnya sebagai teks (string).

```python
# Program akan menampilkan "Siapa namamu? " dan menunggu ketikan pengguna
nama_pengguna = input("Siapa namamu? ")
```
