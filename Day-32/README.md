# 🎂 Day 32 - Automated Birthday Wisher

## 📌 Project Overview

For Day 32 of the 100 Days of Python challenge, I built an automated Birthday Wisher.

The program reads birthday information from a CSV file, checks if someone has a birthday today, randomly selects a birthday letter, and sends a birthday email automatically.

The project is also connected to **GitHub Actions**, allowing the Python script to run automatically on a schedule without needing to run it manually.

## 🛠️ Technologies Used

* Python
* Pandas
* CSV
* SMTP
* GitHub Actions
* GitHub Secrets

## 📚 What I Learned

* Reading CSV files using Pandas
* Working with dates using Python's `datetime` module
* Using `random` to select a birthday message
* Sending emails using `smtplib`
* Using environment variables with `os`
* Protecting sensitive information with GitHub Secrets
* Creating automated workflows with GitHub Actions
* Scheduling Python scripts using cron

## 🔐 Security

I did not store my email address or password directly in the Python code.

Instead, I used environment variables:

```python
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
