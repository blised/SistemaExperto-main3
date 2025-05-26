# Expert System for Archaeological Site Detection

## Overview
This project is an **Expert System** designed to identify archaeological sites in Mexico based on user-provided characteristics. The system uses a predefined dictionary to match input data to known archaeological sites and can handle new entries if no matches are found. 

## Features
- Identify people how succed on something sites based on:
  - Gender (Male or female).
  - Problem (Medical situacion or Social exclusion).
  - A more specifi problem (like gender discrimination or an specific illnes).
  - Field where he/she achieved his/her achievement (futboll, math, etc)
- Display images and descripcions of matched person.
- Justify why a person matches the given characteristics.
- Allow users to add new sites to the database when no matches are found.
- Provide an interactive and user-friendly interface.

---

## Repository Structure

### Folders and Files
- **`app.py`**: Main application file to run the expert system.
- **`config.py`**: Contains configuration settings for the system.
- **`dictionary.py`**: Includes the predefined database of people and their attributes.
- **`personas_logros.json`**: database where all the data is save.
- **`.py`**: Handles user input and validates responses.
- **`__pycache__`**: Auto-generated folder for Python bytecode.

---

## How to Use

### Prerequisites
1. Install Python (version 3.8 or later is recommended).
2. Clone this repository:
   ```bash
   git clone https://github.com/GabrielManzanilla/SistemaExperto.git
