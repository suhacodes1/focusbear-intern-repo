# Writing Unit Tests for Clean Code

## Goal

Learn how writing unit tests helps maintain clean and reliable code.

## Testing Framework Used

For this task, I used Pytest because it is simple to use, readable, and commonly used for testing Python code.

## Function Tested

I created a function called `calculate_task_completion_rate`. This function calculates the percentage of completed tasks based on the total number of tasks.

## Unit Tests Written

I wrote unit tests for:

- A normal completion rate calculation
- A case where total tasks is zero
- A decimal result
- A case where negative values are provided

## Reflection

### 1. How do unit tests help keep code clean?

Unit tests help keep code clean because they make the expected behaviour of a function clear. They also make it easier to check if changes break existing functionality. When writing tests, I had to think about edge cases, which helped me improve the function design.

Unit tests also encourage smaller and more focused functions. If a function is difficult to test, it usually means the function may be doing too much or needs to be simplified.

### 1. What issues did you find while testing?

While testing, I realised that the function needed to handle edge cases properly. For example, if the total number of tasks was zero, the function could cause a division error. I fixed this by returning zero when `total_tasks` is zero.

I also noticed that negative values should not be accepted because completed tasks or total tasks cannot realistically be negative. I added a `ValueError` to handle this case.

## Summary

## This task helped me understand how unit testing improves code quality. By testing normal cases and edge cases, I was able to make the function more reliable, easier to understand, and safer to modify in the future.

# Naming Variables and Functions

## Goal

Learn how to choose clear and meaningful names for variables and functions.

## Best Practices for Naming

Good variable and function names should be clear, descriptive, and easy to understand. A name should explain what the value stores or what the function does without needing extra comments.

Some good naming practices include:

- Use descriptive names instead of short unclear names
- Use verbs for function names, such as `calculate`, `get`, or `validate`
- Use nouns for variable names
- Keep names consistent across the codebase
- Avoid vague names like `data`, `temp`, `x`, or `stuff`

## Example of Poor Naming

```python
def calc(a, b):
    return a / b * 100
```
