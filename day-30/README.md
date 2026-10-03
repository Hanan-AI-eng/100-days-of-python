# 🐍 Python Exception Handling & Error Raising

This project is a simple Python practice program that demonstrates how to **identify, handle, and raise errors** using Python's exception-handling system.

It covers common built-in exceptions such as `FileNotFoundError`, `KeyError`, `IndexError`, and `TypeError`, as well as using `try`, `except`, `else`, `finally`, and `raise`.

## 📚 What I Learned

### 1. FileNotFoundError

Occurs when Python tries to open a file that does not exist.

```python
with open("a_file.txt") as file:
    file.read()
```

If `a_file.txt` does not exist, Python raises:

```text
FileNotFoundError
```

---

### 2. KeyError

Occurs when trying to access a dictionary key that doesn't exist.

```python
a_dic = {"Key": "value"}
cvalue = a_dic["hi"]
```

Since `"hi"` is not a key in the dictionary, Python raises:

```text
KeyError
```

---

### 3. IndexError

Occurs when trying to access an index that is outside the range of a list.

```python
fruit = ["a", "b"]
frui = fruit[3]
```

The valid indexes are `0` and `1`, so accessing index `3` raises:

```text
IndexError
```

---

### 4. TypeError

Occurs when an operation is performed on incompatible data types.

```python
text = "abc"
print(text + 5)
```

A string cannot be directly added to an integer, so Python raises:

```text
TypeError
```

---

## 🛡️ Using try / except

Python allows us to handle errors without immediately stopping the program.

```python
try:
    file = open("a_file.txt")
    a = {"k": "v"}
    print(a["k"])

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("hi bro f")

except KeyError as error_message:
    print(f"That {error_message} key does not exist")

else:
    content = file.read()
    print(content)

finally:
    raise TypeError("hello")
```

### `try`

Contains the code that might cause an exception.

### `except`

Handles a specific exception if one occurs.

### `else`

Runs only when no exception occurs inside the `try` block.

### `finally`

Runs whether an exception occurs or not.

---

## 🚨 Raising Your Own Error

Python also allows us to intentionally raise an exception using `raise`.

In this project, the user's height is checked before calculating BMI:

```python
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
```

If the user enters a height greater than `3` meters, the program intentionally raises:

```text
ValueError
```

This is useful when we want to make sure that user input follows specific rules.

---

## 🧮 BMI Calculation

The BMI is calculated using:

```text
BMI = weight / height²
```

The program expects:

* **Height:** meters
* **Weight:** kilograms

For example:

```text
Height: 1.50
Weight: 50

BMI: 22.22
```

---

## 🎯 Purpose of This Project

This project was created as a Python practice exercise to understand:

* Exceptions
* `try`
* `except`
* `else`
* `finally`
* `raise`
* `ValueError`
* `FileNotFoundError`
* `KeyError`
* `IndexError`
* `TypeError`
* Input validation

## 🚀 How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

Enter your height and weight when prompted.

## 🧠 Key Takeaway

Exception handling allows programs to deal with unexpected situations more safely instead of crashing immediately.

The main structure to remember is:

```python
try:
    # Code that might cause an error

except SomeError:
    # Handle the error

else:
    # Runs if there was no error

finally:
    # Always runs
```

And when we need to intentionally stop the program because the input is invalid:

```python
raise ValueError("Invalid input")
```
