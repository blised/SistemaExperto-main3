# Expert System for Archaeological Site Detection

## Overview
This project is an **Expert System** designed to identify archaeological sites in Mexico based on user-provided characteristics. The system uses a predefined dictionary to match input data to known archaeological sites and can handle new entries if no matches are found. 

## Features
- Identify archaeological sites based on:
  - Civilization (e.g., Maya, Aztec, Olmec).
  - genero (e.g., mountainous, valley, caves).
  - Main structures (e.g., pyramids, temples, observatories).
- Display images and descripcions of matched sites.
- Justify why a site matches the given characteristics.
- Allow users to add new sites to the database when no matches are found.
- Provide an interactive and user-friendly interface.

---

## Repository Structure

### Folders and Files
- **`app.py`**: Main application file to run the expert system.
- **`config.py`**: Contains configuration settings for the system.
- **`dictionary.py`**: Includes the predefined database of archaeological sites and their attributes.
- **`.py`**: Handles user input and validates responses.
- **`__pycache__`**: Auto-generated folder for Python bytecode.

---

## How to Use

### Prerequisites
1. Install Python (version 3.8 or later is recommended).
2. Clone this repository:
   ```bash
   git clone https://github.com/GabrielManzanilla/SistemaExperto.git
