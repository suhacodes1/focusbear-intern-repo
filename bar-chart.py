import matplotlib.pyplot as plt

features = ["Focus Timer", "Habit Tracker", "Analytics"]
usage = [50, 35, 20]

plt.bar(features, usage)
plt.title("Feature Usage")
plt.xlabel("Feature")
plt.ylabel("Usage Count")
plt.show()