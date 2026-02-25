from typing import Dict

# Conversion factors for length units (relative to meters)
LENGTH_FACTORS: Dict[str, float] = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1.0,
    "kilometer": 1000.0,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344,
}

# Conversion factors for weight units (relative to grams)
WEIGHT_FACTORS: Dict[str, float] = {
    "milligram": 0.001,
    "gram": 1.0,
    "kilogram": 1000.0,
    "ounce": 28.3495,
    "pound": 453.592,
}

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a length value from one unit to another.

    Args:
        value (float): The numeric value to convert.
        from_unit (str): The unit to convert from.
        to_unit (str): The unit to convert to.

    Returns:
        float: The converted value in the target unit.

    Raises:
        KeyError: If the provided units are not supported.
    """
    meters = value * LENGTH_FACTORS[from_unit]
    return meters / LENGTH_FACTORS[to_unit]

def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a weight value from one unit to another.

    Args:
        value (float): The numeric value to convert.
        from_unit (str): The unit to convert from.
        to_unit (str): The unit to convert to.

    Returns:
        float: The converted value in the target unit.

    Raises:
        KeyError: If the provided units are not supported.
    """
    grams = value * WEIGHT_FACTORS[from_unit]
    return grams / WEIGHT_FACTORS[to_unit]

def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a temperature value between Celsius, Fahrenheit, and Kelvin.

    Args:
        value (float): The temperature value to convert.
        from_unit (str): The unit to convert from ('Celsius', 'Fahrenheit', or 'Kelvin').
        to_unit (str): The unit to convert to ('Celsius', 'Fahrenheit', or 'Kelvin').

    Returns:
        float: The converted temperature value.

    Raises:
        ValueError: If the provided units are not supported.
    """
    # Convert from the source unit to Celsius
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:
        raise ValueError("Unsupported temperature unit")

    # Convert from Celsius to the target unit
    if to_unit == "Celsius":
        return celsius
    elif to_unit == "Fahrenheit":
        return celsius * 9 / 5 + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    else:
        raise ValueError("Unsupported temperature unit")