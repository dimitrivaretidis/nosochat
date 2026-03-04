from flask import Flask, request, render_template_string

app = Flask(__name__)
messages = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>School Chat</title>
</head>
<body>
    <h2>Python Chat</h2>
    <form method="POST">
        <input name="msg" autocomplete="off">
        <input type="submit">
    </form>
    <hr>
    {% for m in messages %}
        <p>{{m}}</p>
    {% endfor %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        messages.append(request.form["msg"])
    return render_template_string(HTML, messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)