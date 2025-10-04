from flask import Flask, render_template, request, jsonify
from pipeline_engine import generate_pipeline_code  # your existing logic

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    instruction = data.get('instruction', '')

    if not instruction.strip():
        return jsonify({'code': "# No instruction provided"})

    try:
        # Call your actual pipeline logic
        generated_code = generate_pipeline_code(instruction)

        return jsonify({'code': generated_code})

    except Exception as e:
        return jsonify({'code': f"# Error generating code: {str(e)}"})

# On Render, remove this line; Gunicorn handles app startup
if __name__ == "__main__":
    app.run(debug=True)

