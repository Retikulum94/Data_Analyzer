from datetime import datetime
import pytz

def calculate_bmi(height, weight):
    """
    Calculate BMI and return a dictionary with inputs, BMI, category, and timestamp.

    Args:
        height (float): Height in meters.
        weight (float): Weight in kilograms.

    Returns:
        dict: A dictionary containing the inputs, calculated BMI, category, and timestamp.
    """
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive values.")

    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = 'Untergewicht'
    elif bmi < 25:
        category = 'Normalgewicht'
    elif bmi < 30:
        category = 'Übergewicht'
    else:
        category = 'Adipositas'

    return {
        "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),  # Current swiss time
        "height": height,
        "weight": weight,
        "bmi": round(bmi, 1),
        "category": category,
    } 