# 📊 06: The Basic Data Types

Every piece of data in Python has a ‘type’ or data type. This is important so that Python knows how to process the data. Basic (primitive) data types are the foundation of all more complex data.

### The Four Basic Building Blocks

Let's meet the four most important data types in Python.

1.  **🔢 Integer (`int`)**: These are whole numbers, without any decimal points. You use them for counting things that can't be split into pieces, like your age or the score in a game.

    - Examples: `10`, `-50`, `2025`

2.  **🔢 Float (`float`)**: These are numbers _with_ a decimal point. Think of them for things you can measure or divide into parts, like weight body and height body.

    - Examples: `3.14`, `129.9`, `0.5`

3.  **🔤 String (`str`)**: We've already met this one! It's any collection of characters or text. The golden rule is that strings must always be wrapped in quotes (`"` or `'`).

    - Examples: `"Hello Bagus!"`, `'Python is fun!'`, `"123"` (This is text, not a number!)

4.  **💡 Boolean (`bool`)**: This one is special and very powerful! A Boolean is like a light switch—it can only have two values: `True` (On/Yes) or `False` (Off/No). Booleans are perfect for checking if something is true or asking yes/no questions.
    - Examples: `is_raining = True`, `game_over = False`

### check type data

```python
num = 12
name = "Bagus"
print(f"num type: {type(num)}")
print(f"name type: {type(name)}")
```
