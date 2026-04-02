import matplotlib.pyplot as plt

session_length = [10, 20, 30, 40, 50]
tasks_completed = [1, 2, 3, 3, 5]

plt.scatter(session_length, tasks_completed)
plt.title("Session Length vs Tasks Completed")
plt.xlabel("Session Length (minutes)")
plt.ylabel("Tasks Completed")
plt.show()