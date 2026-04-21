# Data Manipulation with Pandas

## What is Pandas?

Pandas is a powerful Python library used for data analysis and data manipulation. It allows users to work with structured data in tables called DataFrames. Pandas is widely used by data analysts, scientists, and engineers to clean data, transform information, calculate statistics, and generate insights quickly.

Common uses of Pandas include:

- Loading CSV, Excel, and JSON files
- Filtering rows and selecting columns
- Sorting data
- Grouping and aggregating values
- Cleaning missing or incorrect data
- Merging multiple datasets
- Preparing data for visualisation or machine learning

---

## Load a Dataset into a DataFrame

```python
import pandas as pd

data = {
    "User": ["Alice", "Bob", "Charlie", "David"],
    "Focus_Hours": [5, 3, 6, 2],
    "Tasks_Completed": [8, 4, 10, 3]
}

df = pd.DataFrame(data)

print(df)
```
