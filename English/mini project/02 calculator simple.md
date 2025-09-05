**Create a file named `simple_calculator.py` and copy this code:**

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"\n--- Simple Calculator ---")
print(f"First number: {num1}")
print(f"Second number: {num2}")
print("----------------------------")

# Let's do the math!
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 # Division in Python almost always results in a float!

# We use an f-string to print the result and type() to show its data type.
print(f"Addition result: {addition})")
print(f"Subtraction result: {subtraction})")
print(f"Multiplication result: {multiplication}")
print(f"Division result: {division}")
```
