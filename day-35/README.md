# Weather Alert App ☔🌤️

A Python weather notification application that checks the weather forecast using the **OpenWeatherMap API** and sends a notification when rain is expected.

This project was created as part of the **100 Days of Code: The Complete Python Pro Bootcamp**, Day 35.

## 🚀 Features

- Gets weather forecast data from OpenWeatherMap
- Uses an API key for authentication
- Checks whether rain is expected in the next 12 hours
- Uses weather condition IDs to detect rain
- Sends an SMS notification using the Twilio API
- Supports WhatsApp notifications as an alternative to SMS
- Uses environment variables to protect API keys
- Can be automated to run periodically

## 🛠️ Technologies Used

- Python
- Requests
- OpenWeatherMap API
- Twilio API
- SMS
- WhatsApp
- REST APIs
- JSON
- Environment Variables

## 📚 What I Learned

### API Authentication

Learned how APIs use authentication to control access to their services.

The OpenWeatherMap API requires an API key:

```python
api_key = "YOUR_API_KEY"
