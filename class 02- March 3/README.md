# 🐍 Python Operators

This section covers different types of **operators in Python** with simple examples.

---

## 🔹 1. Arithmetic Operators

Used for basic math operations.

| Operator | Description       | Example   | Output |
|----------|-------------------|-----------|--------|
| `+`      | Addition           | `5 + 3`   | `8`    |
| `-`      | Subtraction        | `10 - 4`  | `6`    |
| `*`      | Multiplication     | `6 * 7`   | `42`   |
| `/`      | Division           | `20 / 4`  | `5.0`  |
| `//`     | Floor Division     | `17 // 3` | `5`    |
| `%`      | Modulus (remainder)| `17 % 3`  | `2`    |
| `**`     | Exponentiation     | `2 ** 3`  | `8`    |

---

## 🔹 2. Comparison Operators

Compare two values and return `True` or `False`.

| Operator | Description       | Example   | Output   |
|----------|-------------------|-----------|----------|
| `==`     | Equal to           | `5 == 5`  | `True`   |
| `!=`     | Not equal to       | `4 != 3`  | `True`   |
| `>`      | Greater than       | `10 > 7`  | `True`   |
| `<`      | Less than          | `3 < 5`   | `True`   |
| `>=`     | Greater or equal   | `5 >= 5`  | `True`   |
| `<=`     | Less or equal      | `2 <= 3`  | `True`   |

---

## 🔹 3. Logical Operators

Combine multiple conditions.

| Operator | Description                 | Example         | Output |
|----------|-----------------------------|-----------------|--------|
| `and`    | Both must be true           | `True and False`| `False`|
| `or`     | At least one must be true   | `True or False` | `True` |
| `not`    | Inverts the result          | `not True`      | `False`|

---

## 🔹 4. Assignment Operators

Assign values to variables.

| Operator | Example     | Same As     |
|----------|-------------|-------------|
| `=`      | `x = 5`     | `x = 5`     |
| `+=`     | `x += 3`    | `x = x + 3` |
| `-=`     | `x -= 2`    | `x = x - 2` |
| `*=`     | `x *= 4`    | `x = x * 4` |
| `/=`     | `x /= 2`    | `x = x / 2` |
| `%=`     | `x %= 2`    | `x = x % 2` |
| `//=`    | `x //= 2`   | `x = x // 2`|
| `**=`    | `x **= 2`   | `x = x ** 2`|
| `&=`     | `x &= 2`    | `x = x & 2` |
| `|=`     | `x |= 2`    | `x = x | 2` |
| `^=`     | `x ^= 2`    | `x = x ^ 2` |

---

## 🔹 5. Identity Operators

Check memory location.

| Operator | Example       | Output   |
|----------|---------------|----------|
| `is`     | `x is y`      | `True` if x and y refer to the same object |
| `is not` | `x is not y`  | `True` if not the same object |

---

## 🔹 6. Membership Operators

Check if a value exists in a sequence.

| Operator | Example               | Output   |
|----------|-----------------------|----------|
| `in`     | `'a' in 'apple'`      | `True`   |
| `not in` | `'x' not in 'apple'`  | `True`   |

---

## 🔹 7. Bitwise Operators

Work at the binary level (0s and 1s).

| Operator | Description         | Example     | Binary Result | Decimal |
|----------|---------------------|-------------|----------------|---------|
| `&`      | AND                 | `5 & 3`     | `0101 & 0011` → `0001` | `1` |
| `|`      | OR                  | `5 | 3`     | `0101 | 0011` → `0111` | `7` |
| `^`      | XOR (exclusive OR)  | `5 ^ 3`     | `0101 ^ 0011` → `0110` | `6` |
| `~`      | NOT (invert bits)   | `~5`        | `~0101` → `1010` (in 2's complement: -6) | `-6` |
| `<<`     | Left Shift          | `5 << 1`    | `0101 << 1` → `1010`   | `10` |
| `>>`     | Right Shift         | `5 >> 1`    | `0101 >> 1` → `0010`   | `2` |

> ⚠️ Note: Bitwise operators are usually used in low-level programming, hardware control, and performance-sensitive tasks.



