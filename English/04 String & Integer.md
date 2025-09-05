# 📝 04: Words and Numbers (Strings & Integers)

In Python, the computer needs to know what _kind_ of information it's working with. The two most common types are **Strings** (which are just text) and **Integers** (which are whole numbers).

### What is a String? (The Words)

A `String` is anything that is text. Think of it as a string of letters, numbers, or symbols all tied together.

**The Golden Rule:** To tell Python that something is a string, you **must** wrap it in quotes. You can use single quotes (`'`) or double quotes (`"`).

```python
# Both of these are valid strings
print("This is a string.")
print('This is also a string.')
print("Even the number 123 is a string if it's inside quotes!")
```

### What is an Integer? (The Numbers)

An `Integer` is a whole number (a number without a decimal point). You use integers for counting and doing math.

Notice that integers **do not use quotes**.

```python
# This is an Integer
print(5)

# Python can do math with integers!
print(100 + 50)
```

### The Big Difference: "5" vs. 5 💡

This is super important! To Python, `"5"` is a text character, while `5` is a number you can do math with.

Watch what happens when we try to "add" them:

```Python
# Adding two INTEGERS (Numbers)
# Python will do the math.
print(5 + 5)
# Expected Output: 10


# Adding two STRINGS (Text)
# Python will just stick them together.
print("5" + "5")
# Expected Output: 55
```

See the difference? One does a calculation, and the other just combines the text.
