<!-- cspell:words dotenv PostgreSQL getenv -->

# Using .env to Keep Database Credentials Secret in Jupyter

## Why is it more secure to use a .env file for database credentials instead of hardcoding them?

Using a `.env` file is more secure because it keeps sensitive information like database usernames, passwords, and API keys separate from the main codebase. If credentials are hardcoded directly into the code, they can easily be exposed when the code is shared, uploaded to GitHub, or accessed by others.

Key security benefits:

- **Prevents accidental exposure:** credentials are not visible in source code
- **Safer version control:** `.env` files can be excluded using `.gitignore`
- **Easier credential rotation:** values can be updated without changing the code
- **Environment separation:** different credentials can be used for development, testing, and production

Hardcoding credentials increases the risk of leaks, especially in collaborative or public repositories. Using a `.env` file follows best practices for secure development.

## How can python-dotenv simplify managing environment variables in Jupyter?

The `python-dotenv` package makes it easy to load environment variables from a `.env` file into a Python environment, including Jupyter Notebooks. Instead of manually setting environment variables each time, `python-dotenv` automatically reads the `.env` file and makes the values accessible in the code.

Benefits of using `python-dotenv`:

- **Automatic loading:** reads all variables from the `.env` file with a single command
- **Cleaner code:** avoids hardcoding credentials in scripts or notebooks
- **Improved readability:** keeps configuration separate from logic
- **Consistency:** ensures the same variables are used across different environments

Example usage in a Jupyter Notebook:

```python
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Access variables
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")

print(db_user)
```
