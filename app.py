import os
from flask import Flask, render_template, request
from model import process_text  # Your model function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        text = request.form['text']  # Get input text from the form
        result = process_text(text)  # Process the text

    return render_template('index.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Heroku's provided port
    app.run(host="0.0.0.0", port=port, debug=True)
