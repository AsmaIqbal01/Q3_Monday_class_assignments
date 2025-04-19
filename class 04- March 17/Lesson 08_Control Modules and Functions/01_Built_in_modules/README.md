## 🔹 What Are Built-in Modules?

**Built-in modules** are pre-installed with Python. You don’t need to install them separately — just `import` and use them directly in your code.

These modules help you:

✅ Work with files and folders  
✅ Perform mathematical operations  
✅ Handle dates and times  
✅ Interact with the operating system  
✅ Generate random numbers  
✅ Manage system-specific parameters and functions  
... and much more!

---

### 🔸 Common Built-in Modules with Examples

#### 📐 `math` – Perform mathematical operations

import math

print(math.sqrt(16))        # Output: 4.0
print(math.pi)              # Output: 3.141592653589793
print(math.factorial(5))    # Output: 120

🎲 random – Generate random numbers

import random

print(random.randint(1, 10))         # Output: Random number between 1 and 10
print(random.choice(['a', 'b', 'c']))# Output: Random element from list

🗂️ os – Interact with the Operating System
import os

print(os.name)                      # Output: 'posix' (Linux/Mac), 'nt' (Windows)
print(os.getcwd())                  # Output: Current working directory
os.mkdir("new_folder")              # Create a new folder

🖥️ sys – System-specific info and control

import sys
print(sys.version)                  # Output: Python version
print(sys.platform)                 # Output: OS platform (like 'win32', 'linux')

✅ Summary Table
| Module   | Purpose                          | Mutable | Example Functions                    |
|----------|----------------------------------|---------|--------------------------------------|
| math     | Math operations                  | No      | `math.sqrt()`, `math.pi`, `factorial()` |
| random   | Random number generation         | No      | `random.randint()`, `random.choice()`  |
| os       | OS-level tasks (folders/files)   | Yes     | `os.getcwd()`, `os.mkdir()`, `os.name` |
| sys      | Python runtime environment       | No      | `sys.version`, `sys.exit()`, `sys.platform` |
| time     | Time-related functions           | No      | `time.sleep()`, `time.time()`         |
| datetime | Date and time manipulation       | Yes     | `datetime.datetime.now()`, `timedelta` |
