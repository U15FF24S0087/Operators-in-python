# Operators-in-python

Python operators perform calculations, compare values, and combine or test data.

## 1. Arithmetic Operators

Arithmetic operators work with numbers:

| Operator | Meaning | Example |
| --- | --- | --- |
| `+` | Add | `5 + 2` gives `7` |
| `-` | Subtract | `5 - 2` gives `3` |
| `*` | Multiply | `5 * 2` gives `10` |
| `/` | Divide; returns a float | `5 / 2` gives `2.5` |
| `//` | Floor divide; rounds down | `5 // 2` gives `2` |
| `%` | Remainder after division | `5 % 2` gives `1` |
| `**` | Raise to a power | `5 ** 2` gives `25` |

## 2. Assignment Operators

Assignment operators store values in variables. `=` assigns a value; the
combined operators perform an operation and assign the result:

```python
score = 10
score += 3  # same as score = score + 3; score is now 13
score *= 2  # score is now 26
```

Other combined forms include `-=`, `/=`, `//=`, `%=`, and `**=`.

## 3. Comparison Operators

Comparison operators compare two values and produce `True` or `False`:

```python
3 == 3  # equal: True
3 != 4  # not equal: True
3 < 4   # less than: True
3 >= 4  # greater than or equal: False
```

The full set is `==`, `!=`, `<`, `>`, `<=`, and `>=`.

## 4. Logical Operators

Logical operators combine or reverse conditions:

```python
age >= 18 and has_id  # True only if both conditions are true
is_weekend or is_holiday  # True if either condition is true
not is_open  # reverses the truth value
```

The operators are `and`, `or`, and `not`.

## 5. Identity Operators

`is` and `is not` test whether two names refer to the very same object. Use
`==` when you want to compare values instead.

```python
first = None
first is None  # True
```

## 6. Membership Operators

`in` and `not in` test whether a value is present in a sequence or collection:

```python
"py" in "python"  # True
4 not in [1, 2, 3]  # True
```

## 7. Bitwise Operators

Bitwise operators work on the binary bits of integers:

| Operator | Meaning |
| --- | --- |
| `&` | Bitwise AND |
| `|` | Bitwise OR |
| `^` | Bitwise XOR |
| `~` | Bitwise NOT |
| `<<` | Shift bits left |
| `>>` | Shift bits right |

For example, `5 & 3` gives `1` because the binary values `101` and `011` have
only their rightmost bit set in common.

## 8. Ternary (Conditional) Expression

Python's conditional expression chooses one of two values based on a
condition. It is sometimes called a ternary operator because it uses three
parts:

```python
label = "adult" if age >= 18 else "minor"
```

Python uses this `value_if_true if condition else value_if_false` syntax,
not the `?:` syntax used by some other languages.

## Calculator

Run `python calculator.py` (or `py -3 calculator.py` on Windows) to try a
calculator for addition (`+`), subtraction (`-`), multiplication (`*`),
division (`/`), floor division (`//`), and remainder (`%`).

## Practice Tasks and Solutions

### Task 1: Arithmetic Calculator

**Question:** Create a calculator that takes two numbers and an operator, then
performs addition, subtraction, multiplication, division, floor division, or
remainder.

**Solution:** The `calculate` function selects the operation from the operator
and rejects unsupported operators or division by zero. See [calculator.py](calculator.py).

### Task 2: Number Properties

**Question:** Given an integer, determine whether it is even or odd and whether
it is divisible by 3 and by 5.

**Solution:** `check_number` uses `%` to return the number's parity and two
divisibility results. See [check_number.py](check_number.py).

### Task 3: Marks Result

**Question:** Return `Distinction` for marks of 75 or more, `Pass` for marks
from 35 up to (but not including) 75, and `Fail` for marks below 35.

**Solution:** `check_result` checks the distinction threshold first, then the
pass threshold. See [check_result.py](check_result.py).

### Task 4: Student Eligibility

**Question:** A student is eligible when marks are at least 60, attendance is
at least 75%, and the student has no backlog.

**Solution:** `check_eligibility` combines the three requirements with `and`.
See [check_eligibility.py](check_eligibility.py).

### Task 5: Username and Password

**Question:** Validate a user when the username is `admin` and the password is
`python123`.

**Solution:** `validate_user` compares both values and returns `Valid` only
when both match. This hard-coded credential check is for practice, not secure
authentication. See [validate_user.py](validate_user.py).

### Task 6: Purchase Discount

**Question:** Apply a 20% discount to purchases of Rs. 5,000 or more, 10% to
purchases from Rs. 3,000 through Rs. 4,999, and 5% to lower non-negative
amounts. Return the discount and final payable amount.

**Solution:** `calculate_discount` chooses the rate, calculates the discount,
and returns `(discount_amount, final_amount)`. See [calculate_discount.py](calculate_discount.py).

### Task 7: Access Check

**Question:** Grant access when the person is at least 18 and has an ID, or
when the person is an employee.

**Solution:** `check_access` implements `(age >= 18 and has_id) or is_employee`.
See [check_access.py](check_access.py).

### Task 8: Skill Lookup

**Question:** Check whether a requested skill is in the list
`["python", "SQL", "git", "html"]` and display whether it is available.

**Solution:** `check_skill` searches the list without regard to letter case
and returns an availability message. See [check_skill.py](check_skill.py).

### Task 9: Calculator Function

**Question:** Create `calculate(a, operator, b)` to support `+`, `-`, `*`,
`/`, `//`, and `%`, and handle invalid operators and division by zero.

**Solution:** `calculate` returns the requested arithmetic result, raises
`ValueError` for unsupported operators, and raises `ZeroDivisionError` for a
zero divisor. See [calculate.py](calculate.py).

### Task 10: Placement Eligibility and Category

**Question:** Determine placement eligibility from marks (at least 60),
attendance (at least 75%), and backlog status (no backlog). Categorize
experience `"0"` as Fresher, `"1-2"` as Junior, and `">2"` as Experienced.

**Solution:** `determine_placement` returns the eligibility result and mapped
category. Age is accepted as an argument, but no age eligibility rule was
specified, so it does not affect the result. See [determine_placement.py](determine_placement.py).