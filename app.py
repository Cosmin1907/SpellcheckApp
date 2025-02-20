import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS
from model import process_text  # Your model function

app = Flask(__name__)
CORS(app)  # 🔥 Enable CORS for all routes (required for WordPress)

# 🖥️ Web interface (existing route)
@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        text = request.form['text']  # Get input from the form
        result = process_text(text)  # Process text

    return render_template('index.html', result=result)

# 🔗 API Endpoint (for external apps like WordPress)
@app.route('/api/process_text', methods=['POST'])
def api_process_text():
    data = request.json  # Get JSON data from request
    text = data.get('text', '')  # Extract the text field

    if not text:
        return jsonify({'error': 'No text provided'}), 400  # Return error if empty

    result = process_text(text)  # Process the text

    return jsonify({'result': result})  # Send back the response

# 📩 Handle text input from HTMX (WordPress)
@app.route('/process_text', methods=['POST'])
def process_text_route():
    text = request.form.get('text', '')  # Get input text
    if not text:
        return "<p class='error'>Please enter some text.</p>", 400  # Handle empty input

    result = process_text(text)  # Process the input using your function
    return f"<p class='result'>{result}</p>"  # Return updated HTML snippet

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Heroku's provided port
    app.run(host="0.0.0.0", port=port, debug=True)
