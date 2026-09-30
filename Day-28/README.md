# 🍅 Pomodoro Timer

A simple **Pomodoro Timer desktop application** built with **Python and Tkinter**.

This project implements the Pomodoro technique by alternating between focused work sessions and short/long breaks. It also keeps track of completed work sessions using check marks.

## 📌 About the Project

The Pomodoro technique divides study or work into focused time intervals followed by breaks.

This application uses:

* **25 minutes** of work
* **5 minutes** of short break
* **20 minutes** of long break after 4 work sessions

The timer automatically switches between work and break sessions.

---

## ✨ Features

* 🍅 Pomodoro-style timer interface
* ⏱️ 25-minute work sessions
* ☕ 5-minute short breaks
* 🌙 20-minute long break
* 🔄 Automatically switches between work and break sessions
* ✅ Displays completed work sessions with check marks
* 🔁 Reset button to restart the timer
* 🎨 Color changes depending on the current session
* 🖼️ Tomato image displayed using Tkinter Canvas

---

## 🛠️ Technologies Used

* **Python**
* **Tkinter**
* **Math module**

### Python concepts used

* Functions
* Global variables
* Conditional statements
* `if / elif / else`
* Loops
* Modulo operator `%`
* String formatting
* Tkinter widgets
* Tkinter `Canvas`
* Tkinter `after()` for timer scheduling
* Event-driven programming

---

## 📂 Project Structure

```text
Pomodoro-Timer/
│
├── main.py
├── tomato.png
└── README.md
```

### Files

**`main.py`**

Contains the complete Pomodoro Timer application.

**`tomato.png`**

The tomato image used in the timer interface.

**`README.md`**

Project documentation.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Open the project folder

```bash
cd Pomodoro-Timer
```

### 3. Run the Python file

```bash
python main.py
```

Make sure `tomato.png` is in the same directory as `main.py`.

---

## ⏱️ How the Timer Works

The application uses a repetition counter called `reps`.

```python
reps = 0
```

Every time the Start button is pressed:

```python
reps += 1
```

The program then determines which session should run.

### Work Session

Odd repetitions start a work session:

```python
if reps % 2 != 0:
    count_down(work_sec)
```

The default work duration is:

```python
WORK_MIN = 25
```

### Short Break

Even repetitions normally start a short break:

```python
elif reps % 2 == 0:
    count_down(short_break_sec)
```

The short break duration is:

```python
SHORT_BREAK_MIN = 5
```

### Long Break

After 8 repetitions, the application starts a long break:

```python
if reps % 8 == 0:
    count_down(long_break_sec)
```

The long break duration is:

```python
LONG_BREAK_MIN = 20
```

---

## 🔢 Pomodoro Cycle

The timer follows this general pattern:

```text
Work       → 25 min
Short Break → 5 min
Work       → 25 min
Short Break → 5 min
Work       → 25 min
Short Break → 5 min
Work       → 25 min
Long Break → 20 min
```

Then the cycle repeats.

---

## ⏳ Countdown Mechanism

The countdown is handled by:

```python
def count_down(count):
```

The remaining seconds are converted into minutes and seconds:

```python
count_min = math.floor(count / 60)
count_sec = count % 60
```

The timer display is then updated on the Canvas:

```python
canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
```

The application uses Tkinter's `after()` method to call the countdown function again after 1 second:

```python
time = window.after(1000, count_down, count - 1)
```

This allows the timer to continue counting down without freezing the GUI.

---

## 🔄 Reset Function

The Reset button calls:

```python
reset_timer()
```

The function:

* Cancels the current scheduled timer
* Resets the timer display to `00:00`
* Changes the title back to `Timer`
* Removes the check marks
* Resets the repetition counter to `0`

---

## 🎨 User Interface

The application uses Tkinter's:

* `Tk`
* `Canvas`
* `Label`
* `Button`
* `PhotoImage`

The Canvas is used to display the tomato image and timer:

```python
canvas.create_image(100, 112, image=tomato_pic)

timer = canvas.create_text(
    100,
    130,
    text="00:00",
    font=(FONT_NAME, 35, "bold"),
    fill="white"
)
```

Different colors are used for different timer states:

```text
🟢 Work
🩷 Short Break
🔴 Long Break
```

---

## 🧠 What I Learned

Through this project, I practiced:

* Building a GUI with Tkinter
* Creating and configuring Tkinter widgets
* Using a Canvas to display images and text
* Creating functions for different application behaviors
* Using `global` variables
* Working with timers using `after()`
* Using the modulo operator to control the Pomodoro cycle
* Updating GUI elements dynamically
* Building an event-driven Python application

---

## 📸 Project Preview

Add a screenshot of your application here:

```markdown
![Pomodoro Timer Screenshot](screenshot.png)
```

---

## 🔮 Possible Future Improvements

Some possible improvements include:

* 🔊 Add a sound when a session finishes
* ⏸️ Add a Pause button
* ▶️ Add a Resume button
* ⚙️ Allow users to customize work and break durations
* 💾 Save completed sessions
* 📊 Add daily productivity statistics
* 🎨 Improve the user interface
* 🌙 Add dark mode

---

## 👩‍💻 Author

**Hanan**

Computer Science (Artificial Intelligence) Student

Built with Python 🐍 and Tkinter 🖥️

---

## ⭐ If you like this project

Feel free to star ⭐ the repository and use the project as a starting point for your own Pomodoro Timer.
