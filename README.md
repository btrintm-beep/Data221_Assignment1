****## Repository Overview

This repository contains the Python solutions for **Assignment 1**.
Each question is implemented in a **separate Python file**, follows the assignment instructions, and runs without errors.

The code uses **clear, descriptive variable names** and includes comments to improve readability and understanding.

---

## File Descriptions

### Question 1 — Controlled Multiplication Loop

**File:** `question1.py`
Multiplies consecutive integers starting from 1 until the product exceeds a given threshold value.
The program tracks the current multiplier and prints the final product and the integer that caused the threshold to be exceeded.

---

### Question 2 — Nested Dictionary from Strings

**File:** `question2.py`
Defines a function that takes a list of strings and returns a nested dictionary.
Each string is used as a key, and each value contains:

* The length of the string
* Whether the length is even or odd

---

### Question 3 — Safe Function Application

**File:** `question3.py`
Defines a function to compute ( x^y ).
Processes a list of number pairs using argument unpacking and:

* Skips pairs with negative exponents
* Stores valid results in a list
* Prints the final result list

---

### Question 4 — Sorted Search with Conditions

**File:** `question4.py`
Generates a list of random values between 0 and 1 and a random comparison value.
The program:

* Sorts the list
* Finds all indices where values are greater than or equal to the comparison value
* Prints the sorted list, the comparison value, and the first matching index (if one exists)

---

### Question 5 — Circle Area Comparison with Validation

**File:** `question5.py`
Defines a function that:

* Validates both circle radii as positive integers
* Computes both circle areas
* Returns the percentage of the larger circle’s area that can be covered by the smaller circle
  Returns a meaningful message if invalid input is provided.

---

### Question 6 — Distribution Analysis

**File:** `question6.py`
Defines a function that returns a dictionary where:

* Each key is a unique value from the input list
* Each value is the percentage of numbers less than or equal to that key
  The final dictionary is sorted by key before being returned.

---

### Question 7 — Time Conversion Function

**File:** `question7.py`
Converts a number of seconds since midnight into:

* Hours
* Minutes
* Seconds
* AM/PM format
  Returns a formatted time string or an error message for invalid input.

---

### Question 8 — Pandas DataFrame with Computed Column

**File:** `question8.py`
Creates a Pandas DataFrame from the provided dataset and adds a new computed column derived from existing columns.
Prints the final DataFrame.

---

## Requirements

* Python 3.10+
* Pandas (for Question 8)

To install Pandas:

```bash
pip install pandas
```

---

## Notes

* All files are written to follow the assignment’s formatting and clarity guidelines.
* Variable names are descriptive, and logic is implemented using simple, readable Python constructs.
* Each file can be run independently.


