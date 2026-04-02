<!-- cspell:words Matplotlib Seaborn histplot heatmap pyplot xlabel ylabel -->

# Basic Charting & Data Visualization with Matplotlib & Seaborn

## Why is data visualization important in analytics?

Data visualization is important because it turns raw numbers into visuals that are easier to understand. Instead of reading large tables of data, charts help identify patterns, trends, outliers, and relationships more quickly. Visualizations also make it easier to communicate findings to other people, especially those who may not have a technical background.

In analytics, visualizations help answer questions such as:

- Are users becoming more engaged over time?
- Which features are used the most?
- Are there unusual spikes or drops in activity?
- Is there a relationship between two variables?

At Focus Bear, visualization can help the team understand user behaviour, monitor engagement trends, and make product decisions based on clear evidence rather than assumptions.

## What types of charts are most useful for different types of data?

Different chart types are useful for different purposes:

### Like chart

A line chart is best for showing trends over time.  
Example uses:

- Daily active users over a month
- Weekly focus session completions
- Retention trends over time

### Bar chart

A bar chart is useful for comparing categories.  
Example uses:

- Comparing feature usage counts
- Number of users by subscription type
- Tasks completed across different categories

### Scatter plot

A scatter plot helps show relationships between two numeric variables.  
Example uses:

- Time spent in the app vs. number of tasks completed
- Session length vs. productivity rating
- Age vs. app engagement

### Histogram

A histogram is useful for showing the distribution of one numeric variable.  
Example uses:

- Distribution of focus session lengths
- Distribution of daily task counts
- Distribution of app opens per user

### Heatmap

A heatmap is useful for showing correlations or intensity across values.  
Example uses:

- Correlation between multiple product metrics
- Which days and times have the highest activity
- Patterns in user engagement across categories

## How do Seaborn’s advanced visualizations compare to Matplotlib’s basic charts?

Matplotlib is a general-purpose plotting library that provides strong control over chart creation. It is useful for building basic charts such as line graphs, bar charts, and scatter plots. It gives flexibility, but sometimes requires more code for styling and readability.

Seaborn is built on top of Matplotlib and makes it easier to create more visually appealing and statistically useful charts. It has simpler functions for common analytics tasks, especially when working with distributions and relationships between variables.

Main differences:

### Matplotlib

- Good for basic charts
- Highly customizable
- Gives more low-level control
- Often requires more manual formatting

### Seaborn

- Easier to create polished charts quickly
- Better for statistical graphics
- Works well with Pandas DataFrames
- Includes built-in charts like `histplot` and `heatmap`

In practice, Matplotlib is useful for foundational plotting, while Seaborn is helpful when deeper statistical understanding or cleaner styling is needed.

## How could Focus Bear use visualizations to improve product decision-making?

Focus Bear could use visualizations in many ways to better understand users and improve the product.

Examples include:

- **User engagement trends:** line charts could show whether active usage is increasing or decreasing over time
- **Feature usage comparison:** bar charts could compare which tools or features are most used
- **Retention analysis:** line charts or cohort-style visuals could show how many users continue using the app after a certain number of days
- **Session analysis:** histograms could show common focus session lengths
- **Correlation analysis:** heatmaps could reveal relationships between engagement metrics, task completion, and session frequency
- **Experiment results:** charts could help compare product changes before and after a new feature release
- **Friction point detection:** visual drops in usage or completion could highlight where users struggle

These visualizations help teams make better product decisions because they show patterns clearly and support evidence-based improvements.

## Example Matplotlib charts

### Line chart

```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
active_users = [120, 135, 128, 145, 160]

plt.plot(days, active_users)
plt.title("Daily Active Users")
plt.xlabel("Day")
plt.ylabel("Number of Users")
plt.show()
```
