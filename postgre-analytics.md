# PostgreSQL for Analytics

## 🎯 Goal

Learn how to query and analyze structured data using PostgreSQL.

---

## 📊 Key PostgreSQL Features for Analytics

### 1. Window Functions

Window functions allow calculations across a set of rows related to the current row without grouping them.

Example use:

- Ranking users
- Running totals
- Trend analysis over time

---

### 2. Indexing

Indexes improve query performance by allowing faster data retrieval.

Example:

```sql
CREATE INDEX idx_user_id ON users(user_id);
```
