from flask import Flask, render_template, request
from converters import convert_length, convert_weight, convert_temperature, LENGTH_FACTORS, WEIGHT_FACTORS

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the main page with links to each unit converter.

    Returns:
        str: Rendered HTML for the main page.
    """
    return render_template('base.html')

@app.route('/length', methods=['GET', 'POST'])
def length():
    """
    Handle the length conversion page.
    Processes form submission and displays the conversion result or error.

    Returns:
        str: Rendered HTML for the length converter page.
    """
    result = None
    error = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            result = convert_length(value, from_unit, to_unit)
        except Exception as e:
            error = str(e)
    return render_template(
        'length.html',
        units=LENGTH_FACTORS.keys(),
        result=result,
        error=error
    )

@app.route('/weight', methods=['GET', 'POST'])
def weight():
    """
    Handle the weight conversion page.
    Processes form submission and displays the conversion result or error.

    Returns:
        str: Rendered HTML for the weight converter page.
    """
    result = None
    error = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            result = convert_weight(value, from_unit, to_unit)
        except Exception as e:
            error = str(e)
    return render_template(
        'weight.html',
        units=WEIGHT_FACTORS.keys(),
        result=result,
        error=error
    )

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    """
    Handle the temperature conversion page.
    Processes form submission and displays the conversion result or error.

    Returns:
        str: Rendered HTML for the temperature converter page.
    """
    result = None
    error = None
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            result = convert_temperature(value, from_unit, to_unit)
        except Exception as e:
            error = str(e)
    return render_template(
        'temperature.html',
        units=units,
        result=result,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True)