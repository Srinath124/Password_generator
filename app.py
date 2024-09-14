from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# Password Strength Checker Logic
def check_strength(password):
    score = 0
    if len(password) >= 12:
        score += 20
    if any(c.islower() for c in password):
        score += 20
    if any(c.isupper() for c in password):
        score += 20
    if any(c.isdigit() for c in password):
        score += 20
    if any(c in string.punctuation for c in password):
        score += 20
    return score

# Strong Password Generator
def generate_strong_password(input_text):
    symbols = "!@#$%^&*"
    strong_password = ''.join(random.choice(symbols) if random.random() > 0.5 else char for char in input_text)
    return strong_password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.form['input_text']
    strong_password = generate_strong_password(input_text)
    strength = check_strength(strong_password)
    return jsonify({
        'strong_password': strong_password,
        'strength_score': strength
    })

if __name__ == "__main__":
    app.run(debug=True)
