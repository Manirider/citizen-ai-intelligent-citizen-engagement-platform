from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Load IBM Granite 3.3 2B Instruct Model
model_id = "ibm-granite/granite-3.3-2b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto"
)

# Load Sentiment Pipeline
sentiment_pipeline = pipeline('sentiment-analysis')

# Dummy user for authentication
USER = {'username': 'admin', 'password': 'password'}

# In-memory storage
chat_history = []
concerns = []

# ====================== Static Pages =======================
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    sentiment_counts = {'POSITIVE': 0, 'NEGATIVE': 0, 'NEUTRAL': 0}

    for chat in chat_history:
        sentiment = chat['sentiment'].split(':')[1].split()[0]
        if sentiment in sentiment_counts:
            sentiment_counts[sentiment] += 1

    return render_template(
        'dashboard.html',
        chat_history=chat_history[-5:],
        sentiment_counts=sentiment_counts,
        concerns=concerns[-5:]
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USER['username'] and password == USER['password']:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

# ===================== Chat Routes =========================
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'username' not in session:
        return redirect(url_for('login'))

    response = ""
    sentiment_result = ""
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = generate_response(user_input)
        sentiment_result = analyze_sentiment(user_input)

        chat_history.append({
            'user_input': user_input,
            'response': response,
            'sentiment': sentiment_result
        })

        if sentiment_result.startswith("Sentiment: NEGATIVE"):
            concerns.append({
                'user': session.get('username', 'guest'),
                'concern': user_input
            })

    return render_template('chat.html', response=response, sentiment=sentiment_result)

@app.route('/get_response', methods=['POST'])
def get_response():
    if 'username' not in session:
        return jsonify({'response': 'Unauthorized. Please login first.'})

    user_input = request.json['message']
    response = generate_response(user_input)
    sentiment_result = analyze_sentiment(user_input)

    chat_history.append({
        'user_input': user_input,
        'response': response,
        'sentiment': sentiment_result
    })

    if sentiment_result.startswith("Sentiment: NEGATIVE"):
        concerns.append({
            'user': session.get('username', 'guest'),
            'concern': user_input
        })

    return jsonify({'response': response})

# ====================== Helper Functions ======================
def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return f"Sentiment: {result['label']} (Confidence: {round(result['score'], 2)})"

# ====================== Run Server ======================
if __name__ == '__main__':
    app.run(debug=True)
