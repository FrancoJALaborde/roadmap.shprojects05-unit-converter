# Unit Converter Web Application

A simple web application to convert between different units of measurement: **length**, **weight**, and **temperature**.  
Built with Python and Flask, following best practices, type annotations, and full test coverage.

---

## Features

- Convert between various units of length, weight, and temperature.
- Clean, user-friendly web interface.
- Backend-driven conversion logic (no JavaScript required).
- Robust error handling.
- Fully tested with `pytest`.

---

## Supported Units

### Length
- millimeter
- centimeter
- meter
- kilometer
- inch
- foot
- yard
- mile

### Weight
- milligram
- gram
- kilogram
- ounce
- pound

### Temperature
- Celsius
- Fahrenheit
- Kelvin

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd unit_converter
```
### 2. Install dependencies

It is recommended to use a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```

Open your browser and go to http://localhost:5000


## Usage Examples

### Length Conversion

- Convert 1000 meters to kilometers:
  - Input: 1000
  - From: meter
  - To: kilometer
  - Result: 1.0

### Weight Conversion
- Convert 2 kilograms to grams:
  - Input: 2
  - From: kilogram
  - To: gram
  - Result: 2000.0

### Temperature Conversion
- Convert 0 Celsius to Fahrenheit:
  - Input: 0
  - From: Celsius
  - To: Fahrenheit
  - Result: 32.0

## Running the Tests
All tests are written using pytest.

### 1. Install test dependencies
If not already installed:

```bash
pip install pytest
```

### 2. Run the tests

```bash
pytest
```
You should see all tests passing.

## Project Structure

```bash
unit_converter/
│
├── app.py                # Main Flask application
├── converters.py         # Conversion logic and functions
├── test_app.py           # Test suite for the application
├── requirements.txt      # Python dependencies
└── templates/            # HTML templates
    ├── base.html
    ├── length.html
    ├── weight.html
    └── temperature.html
```

## Extending the Application
- To add more units, update the dictionaries in converters.py.
- To add more conversion types (e.g., area, volume), add new routes, templates, and conversion functions.
