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


high_focus = df[df["Focus_Hours"] > 4]
print(high_focus)



sorted_df = df.sort_values(by="Tasks_Completed", ascending=False)
print(sorted_df)


grouped = df.groupby("User")["Tasks_Completed"].sum()
print(grouped)

df.loc[1, "Focus_Hours"] = None

df["Focus_Hours"] = df["Focus_Hours"].fillna(df["Focus_Hours"].mean())
print(df)


```

### Reflection

1. What are the advantages of using Pandas for data manipulation?

Pandas makes it easier to work with structured data because it provides built-in functions for filtering, sorting, and aggregating data. It reduces the amount of code needed and makes data analysis faster and more efficient.

2. How do you filter and aggregate data in Pandas?

Filtering is done by applying conditions to columns, such as selecting rows where a value meets a condition. Aggregation is done using functions like groupby() combined with operations like sum() or count() to summarise the data.

3. What techniques help handle missing or incorrect data?

Missing data can be handled using functions like fillna() to replace missing values or dropna() to remove them. Incorrect data can be fixed using cleaning methods like replace() or by correcting values manually.

4. How would Pandas be useful for analyzing Focus Bear’s user activity data?

Pandas can be used to analyse Focus Bear’s user data by tracking user activity, focus time, and completed tasks. It can help identify trends such as which users are most active or when usage is highest. This can support better decision-making and product improvements.
