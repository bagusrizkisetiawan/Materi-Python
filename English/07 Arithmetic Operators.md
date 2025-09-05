# 🧮 07: Arithmetic Operators

Python is amazing at math! To do calculations, we use special symbols called **arithmetic operators**. Think of them like the buttons on a super-smart calculator that help us add, subtract, multiply, and more.

### The Main Math Superpowers

Here are the most common operators you'll use:

| Operator | Name                                   | Example  | Result | How to Think About It                  |
| :------- | :------------------------------------- | :------- | :----- | :------------------------------------- |
| `+`      | Addition                               | `5 + 2`  | `7`    | Adding two numbers together.           |
| `-`      | Subtraction                            | `5 - 2`  | `3`    | Taking one number away from another.   |
| `*`      | Multiplication                         | `5 * 2`  | `10`   | Multiplying numbers.                   |
| `/`      | Division                               | `5 / 2`  | `2.5`  | Sharing equally, can have decimals.    |
| `%`      | Modulo (The Remainder)                 | `5 % 2`  | `1`    | What's leftover after dividing?        |
| `**`     | Exponent (Power Up!)                   | `5 ** 2` | `25`   | Multiply a number by itself (`5 * 5`). |
| `//`     | Floor Division (Whole Number Division) | `7 // 2` | `3`    | How many times does it fit completely? |

**Let's look at the tricky ones:**

- **Modulo (`%`)**: Imagine you have 5 cookies (`5`) to share between 2 friends (`2`). Each friend gets 2 cookies, and there is **1** leftover just for you! That's the modulo.
- **Floor Division (`//`)**: Imagine you have 7 slices of pizza (`7`) and you want to put them in boxes that hold 2 slices each (`2`). You can only make **3** full boxes. Floor division ignores the leftovers.

### 💡 Level Up: Python's Order of Operations

Python is smart and follows the same math rules you learn in school, often called **PEMDAS**. This means it does things in a special order:

1.  **P**arentheses `()`
2.  **E**xponents `**`
3.  **M**ultiplication `*` and **D**ivision `/` (from left to right)
4.  **A**ddition `+` and **S**ubtraction `-` (from left to right)

For example, `2 + 3 * 4` will result in `14` (because `3 * 4` is done first), not `20`.

```python
# Python does multiplication first
result1 = 2 + 3 * 4
print(f"2 + 3 * 4 is {result1}") # Output: 14

# Use parentheses to change the order and do addition first!
result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 is {result2}") # Output: 20
```
