import os
from flask import Flask, render_template, request, jsonify
from model import process_text  # Your model function

app = Flask(__name__)

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

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Heroku's provided port
    app.run(host="0.0.0.0", port=port, debug=True)
