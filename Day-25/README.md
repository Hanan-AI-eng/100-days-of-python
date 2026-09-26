# 🇺🇸 U.S. States Game

A Python game where you try to guess all 50 U.S. states on a map.

## 🎮 How It Works

- A blank map of the United States is displayed.
- Enter the name of a state in the input box.
- If the answer is correct, the state name appears on the map.
- Your score is updated after each correct answer.
- Type `Exit` to stop the game.
- When you exit, the states you missed are saved to `States to learn.csv`.

## 🛠️ Technologies Used

- Python
- Turtle
- Pandas

## 📚 What I Practiced

- Reading CSV files with Pandas
- Working with DataFrames and Series
- Filtering data using `.isin()`
- Using `~` to find values that are not in a list
- Using `.iloc[]` to access data
- Creating and saving CSV files with `.to_csv()`
- Working with loops and conditional statements
- Using Turtle to create a simple graphical interface

## 📁 Files

- `main.py` → Main game
- `50_states.csv` → State names and their coordinates
- `blank_states_img.gif` → U.S. map
- `States to learn.csv` → States that were missed during the game

## 🚀 How to Run

Install the required library:

```bash
pip install pandas
