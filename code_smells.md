# Identifying and Fixing Code Smells

## Goal

Learn how to recognize common code smells and refactor them for better readability, maintainability, and performance.

## Code Smells Found

While reviewing the chart files, I noticed several code smells across `bar-chart.py`, `heatmap.py`, `histogram.py`, and `pie-chart.py`.

### Magic Numbers and Strings

Some values such as chart sizes, colours, labels, and file names were hardcoded directly inside the code. This makes the code harder to update because the same values may need to be changed in multiple places.

### Long Functions

Some chart files contained all logic inside one large function or script. This made the code harder to read because data setup, chart configuration, and chart display were all mixed together.

### Duplicate Code

The files repeated similar logic for setting chart titles, labels, figure sizes, and displaying charts. This repeated code could be moved into reusable helper functions.

### Deeply Nested Conditionals

Some logic could become hard to follow if multiple conditions are placed inside each other. Refactoring the code into smaller functions helps reduce this complexity.

### Commented-Out Code

Commented-out code can make files look messy and confusing. It should be removed if it is no longer needed.

### Inconsistent Naming

Some variable names were not clear enough to explain what the data represented. More descriptive names make the code easier to understand.

## Example Before Refactoring

```python
import matplotlib.pyplot as plt

x = ["Mon", "Tue", "Wed", "Thu", "Fri"]
y = [2, 4, 3, 5, 1]

plt.figure(figsize=(8, 5))
plt.bar(x, y)
plt.title("Chart")
plt.xlabel("Days")
plt.ylabel("Values")
plt.show()


import matplotlib.pyplot as plt

CHART_SIZE = (8, 5)
DAYS_OF_WEEK = ["Mon", "Tue", "Wed", "Thu", "Fri"]


def create_bar_chart(days, focus_hours):
    plt.figure(figsize=CHART_SIZE)
    plt.bar(days, focus_hours)
    plt.title("Focus Hours by Day")
    plt.xlabel("Day")
    plt.ylabel("Focus Hours")
    plt.show()


daily_focus_hours = [2, 4, 3, 5, 1]

create_bar_chart(DAYS_OF_WEEK, daily_focus_hours)
```

### Refactoring Improvements

I improved the code by:

Replacing unclear variable names with descriptive names
Using constants instead of hardcoded values
Creating reusable functions for chart creation
Removing unnecessary commented-out code
Keeping functions small and focused
Making labels and titles more meaningful
Reflection

### 1. What code smells did you find in your code?

I found magic numbers, duplicate code, unclear variable names, and long functions. The chart scripts repeated similar setup code and used non-descriptive variable names like x and y.

### 2. How did refactoring improve the readability and maintainability of the code?

Refactoring improved readability by making variable names more meaningful and breaking code into smaller functions. Using constants made it easier to update values without searching through the entire file. The code is now easier to understand and reuse.

### 3. How can avoiding code smells make future debugging easier?

Avoiding code smells makes debugging easier because the code is cleaner and more structured. Smaller functions make it easier to locate issues, and removing duplicate code ensures bugs only need to be fixed in one place.
