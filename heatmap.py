import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    "sessions_per_day": [2, 3, 4, 5, 6],
    "tasks_completed": [1, 2, 2, 4, 5],
    "time_in_app": [20, 30, 35, 50, 60]
})

correlation = data.corr()

sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.show()