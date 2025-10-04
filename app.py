from flask import Flask, render_template, request, send_file
from pipeline_engine import parse_instruction, generate_python_code
import tempfile

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    steps = []
    code = ""
    download_path = None
    if request.method == "POST":
        instruction = request.form["instruction"]
        steps = parse_instruction(instruction)
        code = generate_python_code(steps)
        if "download" in request.form:
            # Save generated code into a temporary Python file
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".py")
            with open(tmp.name, "w") as f:
                f.write(code)
            return send_file(tmp.name, as_attachment=True, download_name="generated_pipeline.py")
    return render_template("index.html", steps=steps, code=code)

if __name__ == "__main__":
    app.run(debug=True)
