def calculate_task_completion_rate(completed_tasks, total_tasks):
    if total_tasks == 0:
        return 0

    if completed_tasks < 0 or total_tasks < 0:
        raise ValueError("Task values cannot be negative")

    return round((completed_tasks / total_tasks) * 100, 2)