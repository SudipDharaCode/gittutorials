# app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Enter a Number</title>
<h2>Enter a Number:</h2>
<form method="POST">
  <input name="user_input" type="text">
  <input type="submit">
</form>

{% if result %}
  <h3>You entered: {{ result }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        result = request.form.get("user_input")
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
