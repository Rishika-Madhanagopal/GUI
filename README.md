# MyFirstApp

**MyFirstApp** is a simple graphical user interface (GUI) application built using Python's `tkinter` library. This application allows users to enter personal and academic information, such as ID, name, and marks for three subjects. The data entered can be saved to a CSV file, making it a useful tool for tracking or recording information.

## Features

- **Input Fields**: 
  - ID (integer)
  - Name (text)
  - Marks for three subjects (integer)
- **Gender Selection**: Choose between Male and Female using radio buttons.
- **Country Selection**: Choose among India, UK, and USA with checkboxes.
- **State and Rank Selection**: Choose a state and rank from dropdown menus.
- **Save to CSV**: All data is saved to a CSV file (`mycsv.csv`) upon submission.

## How It Works

1. **Enter Data**: The user fills in the required fields (ID, Name, Marks, etc.).
2. **Select Options**: The user can choose gender, country, state, and rank.
3. **Submit Data**: Upon clicking the "Submit" button, the data is saved to `mycsv.csv` in the project directory.
4. **Output Data**: If the CSV file doesn't exist, it will be created with headers. Otherwise, data is appended to the existing CSV.

## Requirements

- Python 3.x
- `tkinter` library (comes pre-installed with Python)


