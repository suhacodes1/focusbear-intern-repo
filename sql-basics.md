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
