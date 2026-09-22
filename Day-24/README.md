# 💌 Letter Generator

A Python project that automatically creates personalized letters for multiple people.

## 📌 About

This project takes a list of names and a starting letter template, then creates a personalized Word document for each person by replacing `[name]` with their actual name.

## ⚙️ How It Works

1. The program reads the names from `invited_names.txt`.
2. It reads the letter template from `starting_letter.txt`.
3. It replaces `[name]` with each person's name.
4. It creates a separate `.docx` file for each person.
5. The personalized letters are saved in the output folder.

## 🛠️ Technologies

- Python
- File Handling
- String Manipulation
- Microsoft Word Documents

## 📂 Project Structure

```text
Letter-Generator/
│
├── Input/
│   ├── Names/
│   │   └── invited_names.txt
│   │
│   └── Letters/
│       └── starting_letter.txt
│
├── Output/
│   └── ReadyToSend/
│       └── personalized letters
│
└── main.py
