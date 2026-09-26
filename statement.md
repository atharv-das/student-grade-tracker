# Student Grade Tracker — Problem Statement

## Why Build This?
Keeping track of student marks by hand or across messy spreadsheets gets old fast. Cells accidentally get deleted, duplicate IDs slip in, and figuring out who needs extra help ends up taking way more time than it should. 

I built this project to solve that exact headache: a simple, no-nonsense terminal tool to log grades, calculate results automatically, and save everything cleanly to a text file.

---

## What Problem Does It Solve?
* **Messy or lost data:** Saves records directly to `grades.txt` so progress isn't lost when the program closes.
* **Input errors:** Stops duplicate roll numbers, rejects scores outside the 0–100 range, and ignores accidental blank lines or comment rows so the script won't crash.
* **Repetitive math:** Instantly assigns letter grades and calculates class stats like averages, top scores, and lowest scores in seconds.

---

## Key Features
* **Add Students:** Enter a roll number, name, and marks with built-in validation checks.
* **View Full Class:** Prints a formatted summary table showing everyone’s scores and letter grades.
* **Quick Search:** Look up any student by roll number to pull their individual card immediately.
* **Class Insights:** View overall stats to get a quick snapshot of class performance.
* **Persistent Storage:** Everything is loaded from and written back to `grades.txt` automatically.

---

## Grade Scale
Scores are mapped automatically using standard letter grades:

* **A**: 90 – 100
* **B**: 80 – 89.9
* **C**: 70 – 79.9
* **D**: 60 – 69.9
* **F**: Below 60

---

## Built With
* **Language:** Python 3
* **Interface:** Command Line (Terminal / Termux)
* **Storage:** Plain text file (`grades.txt`)
* **Dependencies:** None (runs purely on standard Python)
