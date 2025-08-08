from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Bill Fee Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; text-align: center; }
        input, button { padding: 10px; font-size: 16px; }
        .result { margin-top: 20px; font-weight: bold; font-size: 18px; }
    </style>
</head>
<body>
    <h1>Bill Fee Calculator</h1>
    <form method="post">
        <input type="number" name="amount" placeholder="Enter Bill Amount" required>
        <button type="submit">Calculate</button>
    </form>
    {% if fee is not none %}
        <div class="result">Applicable Fee: ₹{{ fee }}</div>
    {% endif %}
</body>
</html>
"""

def calculate_fee(amount):
    if 4000 <= amount <= 24999:
        return 500
    elif 25000 <= amount <= 99999:
        return 1000
    elif 100000 <= amount <= 299999:
        return 1500
    elif amount >= 300000:
        return 2000
    else:
        return 0

@app.route('/', methods=['GET', 'POST'])
def index():
    fee = None
    if request.method == 'POST':
        try:
            amount = int(request.form['amount'])
            fee = calculate_fee(amount)
        except ValueError:
            fee = "Invalid amount"
    return render_template_string(HTML_TEMPLATE, fee=fee)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
