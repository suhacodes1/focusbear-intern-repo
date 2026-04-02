import seaborn as sns
import matplotlib.pyplot as plt

focus_sessions = [15, 20, 25, 25, 30, 35, 40, 45, 50, 60]

sns.histplot(focus_sessions, bins=5)
plt.title("Distribution of Focus Session Lengths")
plt.xlabel("Session Length (minutes)")
plt.ylabel("Frequency")
plt.show()