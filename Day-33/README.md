# 🌦️ Rain Alert Weather App

A Python weather notification application built as part of the **100 Days of Code: The Complete Python Pro Bootcamp**.

The project uses the **OpenWeatherMap API** to check the weather forecast and sends a notification when rain is expected.

---

## 🚀 Features

- 🌐 Makes API requests using Python
- 🔑 Uses API keys for authentication
- 🌤️ Gets weather forecast data from OpenWeatherMap
- 🌧️ Checks whether rain is expected
- 📱 Sends SMS notifications using Twilio
- 💬 Supports WhatsApp notifications
- 🔐 Uses environment variables to protect API credentials
- ⏰ Can be automated to run periodically

---

## 🛠️ Technologies Used

- Python
- Requests
- REST APIs
- OpenWeatherMap API
- Twilio API
- JSON
- HTTP
- Environment Variables
- GitHub Actions

---

## 📚 What I Learned

### Day 33: APIs

This project started with learning the fundamentals of APIs and how applications communicate with external services.

Topics covered:

- What APIs are
- API endpoints
- Making API calls
- HTTP requests
- HTTP status codes
- Handling exceptions
- Working with JSON data
- API parameters
- REST APIs

### Making API Calls

Python's `requests` library was used to communicate with APIs:

```python
response = requests.get(url)
