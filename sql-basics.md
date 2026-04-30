# Introduction to SQL for Data Analysis

## 🎯 Goal

Learn the fundamentals of SQL, including querying, filtering, and aggregating data for analytics.

---

## 📊 SQL Basics for Analytics

SQL (Structured Query Language) is used to interact with relational databases like PostgreSQL. It allows us to retrieve, filter, sort, and analyze structured data efficiently.

---

## 🧩 SQL Examples

### 1. SELECT Query (Retrieve Data)

```sql
SELECT *
FROM users;

SELECT *
FROM activities
WHERE activity_type = 'login';

SELECT *
FROM activities
ORDER BY activity_date DESC;

SELECT user_id, COUNT(*) AS total_activities
FROM activities
GROUP BY user_id;

SELECT user_id, COUNT(*) AS total_activities
FROM activities
GROUP BY user_id
HAVING COUNT(*) > 50;
```

### Reflection

1. How does SQL help in data analysis?

SQL helps in data analysis by allowing us to quickly retrieve and manipulate structured data stored in databases. It enables filtering, sorting, and aggregating large datasets efficiently, which is essential for generating insights such as user behavior patterns and trends.

2. What is the difference between filtering (WHERE) and aggregation (GROUP BY)?

WHERE is used to filter rows before any grouping or aggregation happens. It selects specific records based on conditions. GROUP BY, on the other hand, groups rows together based on a column and is used with aggregate functions like COUNT, SUM, or AVG to summarize data.

3. How would you retrieve and analyze user activity data in Focus Bear’s database?

I would query the activities table and use SELECT to retrieve relevant columns such as user_id, activity_type, and activity_date. Then I would use WHERE to filter specific activities if needed, ORDER BY to sort them by date, and GROUP BY to analyze patterns like total activities per user. This would help identify trends such as highly active users or peak usage times.

4. Why is learning SQL important even if you primarily use Python for analytics?

Even when using Python, SQL is still important because most data is stored in databases. SQL is often used to extract and preprocess data before loading it into Python tools like Pandas. Knowing SQL makes data retrieval faster and more efficient, and allows better integration between databases and analytics workflows.
