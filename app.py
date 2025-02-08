import os
from flask import Flask, render_template, request, jsonify
from model import process_text  # Your model function

app = Flask(_name)  # ✅ FIXED: Changed _name to _name_

# 🖥 Web interface (existing route)
@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        text = request.form.get('text', '')  # Get input from form
        result = process_text(text)  # Process text
    return render_template('index.html', result=result)

# 🔗 API Endpoint (for external apps like WordPress)
@app.route('/api/process_text', methods=['POST'])
def api_process_text():
    try:
        # ✅ Ensure JSON parsing always works
        data = request.get_json(force=True)  

        if not data or "text" not in data:
            return jsonify({'error': 'No text provided'}), 400  # Return error if empty
        
        text = data['text'].strip()  # Extract and clean text

        result = process_text(text)  # Process the text

        return jsonify({'result': result})  # ✅ CHANGED BACK TO "result" (was "reply")

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Catch any unexpected errors

if _name_ == '_main':  # ✅ FIXED: Changed _name to _name_
    port = int(os.environ.get("PORT", 5000))  # Use Heroku's provided port
    app.run(host="0.0.0.0", port=port, debug=True)