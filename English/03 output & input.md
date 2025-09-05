# 🖨️ 03: Talking to Your Program (Using `print` and `input`)

A computer program is a bit like having a conversation. It usually follows three simple steps:

1.  **Input**: The program gets information (like you typing your name).
2.  **Process**: The program thinks about that information.
3.  **Output**: The program shows a result (like saying "Hello!" back to you).

In this lesson, we'll focus on **Input** and **Output**.

### Making the Computer Talk with `print()`

`print()` is a special command, or **function**, in Python. Its job is to show any message you want on the screen. Whatever you put inside the parentheses `()` is what it will show!

When you want to print text, you must put it inside quotation marks `""`. For numbers, you don't need quotes.

```python
# The computer will show the text on the screen
print("Hello, this is my first message!")

# The computer will show the number
print(12345)
```

### Letting the Computer Listen with `input()`

`input()` is a function that makes your program pause and wait for the user to type something. It's like asking a question and listening for an answer.

The message you put inside the parentheses is the question the computer will ask.

```python
# The program will display "What is your name? " and wait for you to type.
input("What is your name? ")
```

**Important:** The computer always treats the answer you type in as plain text (programmers call this a string).
