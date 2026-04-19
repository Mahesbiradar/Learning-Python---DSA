# 🔹 Chapter 2: Variables in Python (Detailed Notes)

---

## 🧠 1. What is a Variable?

### 📌 Definition

A variable is a **name given to a value stored in memory**, allowing us to reuse and manipulate data easily. 

---

### 🔑 Key Points

* Acts like a **container for data**
* Avoids repeating values in code
* Created using assignment operator `=`

---

### 💻 Example

```python
pi = 3.14
print(pi)
```

---

### 🧠 Internal Understanding (IMPORTANT ⚠️)

* Variable = **reference (name)**
* Value = **object in memory**

👉 Python does **not store value inside variable**, it stores reference.

---

### 🎯 Interview Insight

* Python variables are **labels pointing to objects**, not memory boxes

---

## 🏷️ 2. Naming Variables

### ✅ Rules

* Must start with letter or `_`
* Can contain letters, digits, `_`
* Case-sensitive

---

### ❌ Invalid Examples

```python
1name = "Error"
user-name = "Error"
if = 10
```

---

### ✅ Best Practices (Very Important)

* Use **descriptive names**

```python
radius = 10   # Good
r = 10        # Bad (not clear)
```

* Use **snake_case**

```python
total_marks = 90
```

---

### 🎯 Interview Tip

Bad naming = **poor readability → rejected in interviews**

---

## 🔄 3. Variable Assignment

---

### 🔹 Single Assignment

```python
x = 10
```

---

### 🔹 Multiple Assignment

```python
a, b, c = 1, 2, 3
```

👉 Cleaner + useful in DSA

---

### 🔹 Same Value Assignment

```python
x = y = z = 0
```

---

### 🔥 Swapping Variables (VERY IMPORTANT)

```python
a = 5
b = 10

a, b = b, a
```

---

### 🎯 Interview Insight

* Frequently asked
* Used in sorting algorithms

---

## 🧠 4. Variable Types & Dynamic Typing

### 📌 Concept

Python is **dynamically typed**

```python
x = 10
x = "Hello"
```

---

### 🔑 Key Points

* No type declaration needed
* Type decided at runtime

---

### ⚠️ Strong Typing (Important)

```python
"10" + 5   # ❌ Error
```

👉 Python does NOT auto-convert types

---

### 🎯 Interview Question

👉 Difference:

* Dynamic typing vs Static typing
* Strong typing vs Weak typing

---

## 🔄 5. Mutability (VERY IMPORTANT CONCEPT 🔥)

---

### 🔹 Immutable Types

* Cannot change after creation
* Examples:

  * int
  * float
  * str
  * tuple

```python
x = 10
x = 20   # new object created
```

---

### 🔹 Mutable Types

* Can change in-place
* Examples:

  * list
  * dict
  * set

```python
lst = [1, 2, 3]
lst.append(4)
```

---

### 🧠 Why Important?

👉 Critical in:

* DSA (lists, arrays)
* Debugging memory issues

---

### 🎯 Interview Trap

* Immutable → new object
* Mutable → same object modified

---

## 🌍 6. Scope of Variables

---

### 🔹 Local Scope

* Inside function

```python
def func():
    x = 10
```

👉 Only accessible inside function

---

### 🔹 Global Scope

```python
x = 10

def func():
    print(x)
```

---

### ⚠️ Global Keyword

```python
x = 10

def func():
    global x
    x = 20
```

---

### 🎯 Interview Insight

* Avoid global variables
* Leads to bugs in large systems

---

## ⚙️ 7. Practical Use Cases

---

### 🔹 1. Configuration

```python
API_KEY = "abc123"
```

---

### 🔹 2. Loop Variables (DSA Important)

```python
for i in range(5):
    print(i)
```

👉 Used in:

* Traversal
* Index tracking

---

### 🔹 3. User Input

```python
name = input("Enter name: ")
```

---

## ⚠️ 8. Common Pitfalls

---

### ❌ 1. Uninitialized Variable

```python
print(x)   # ❌ NameError
```

---

### ❌ 2. Variable Shadowing

```python
x = 10

def func():
    x = 20   # shadows global
```

---

### ❌ 3. Type Confusion

```python
x = "10"
y = 5
print(x + y)  # ❌
```

---

### ❌ 4. Input Mistake (VERY COMMON)

```python
age = input("Enter age: ")
print(age + 5)   # ❌
```

✔ Fix:

```python
age = int(input("Enter age: "))
```

---

## 🎯 Interview + DSA Insights

---

### 🔥 Must Know

* Dynamic typing
* Mutability
* Scope
* Swapping variables

---

### 🧠 DSA Connection

Variables used for:

* Index tracking
* Counters
* Temporary storage
* Swapping elements

---

### ⚠️ Advanced Insight

```python
a = [1, 2]
b = a
b.append(3)

print(a)  # [1, 2, 3]
```

👉 Both refer same object → **important for bugs**

---

# 📊 End-of-Chapter Evaluation

---

## 🧠 Conceptual Questions

1. What is a variable in Python?
2. Explain dynamic typing
3. Difference between mutable and immutable
4. What is variable scope?
5. What happens internally when assigning variables?

---

## 💻 Coding Questions

1. Swap two numbers without temp
2. Take input and print sum
3. Modify a list and observe behavior
4. Create local and global variables
5. Check type of variables

---

## 🎤 Interview Questions

1. What is dynamic typing?
2. Mutable vs Immutable difference
3. What is variable shadowing?
4. Why Python variables are references?
5. Output?

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

---

## 🧩 Tricky Questions

1. Why modifying list affects original variable?
2. Difference between assignment and copy? (preview 👀)

---

# ✅ Final Quick Revision

* Variable = **reference to object**
* Dynamic + Strong typing
* Mutable vs Immutable → VERY IMPORTANT
* Scope → local vs global
* Swapping → Python advantage

