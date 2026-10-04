# 🇫🇷 Flashy - French Vocabulary Flash Card App

A simple **French-English flash card application** built with Python and Tkinter.

The app displays a French word on a flash card, waits for 3 seconds, and then automatically flips the card to show the English translation.

You can then choose whether you **knew the word** or **didn't know it**.

---

## 🎯 Features

- 🇫🇷 Displays French vocabulary words
- 🇬🇧 Shows the English translation after 3 seconds
- 🔀 Randomly selects vocabulary cards
- ✅ Remove words you already know
- ❌ Move to the next word without removing it
- 💾 Saves the remaining words to a CSV file
- 📊 Uses Pandas to manage vocabulary data
- 🖥️ Built with Tkinter GUI

---

## 🛠️ Technologies Used

- **Python**
- **Tkinter** - GUI
- **Pandas** - CSV and data management
- **Random** - Random card selection

---

## 📁 Project Structure

```text
Flashy/
│
├── data/
│   ├── french_words.csv
│   └── words_to_learn.csv
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
│
└── main.py
