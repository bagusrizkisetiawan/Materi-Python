# 🔗 14: Kondisi dengan Operator Logika

Menggunakan operator logika di dalam `if` adalah cara yang sangat efisien untuk menghindari `if` yang terlalu dalam (nested if).

### Perbandingan Kode

**Sebelum (dengan Nested If):**

```python
password = "admin123"
if len(password) >= 8:
    if "123" in password:
        print("Password cukup kuat.")
```

**Sesudah (dengan and):**

```python
password = "admin123"
if len(password) >= 8 and "123" in password:
    print("Password cukup kuat.")
```
