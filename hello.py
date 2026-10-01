from datetime import datetime
from flask import Flask, render_template, redirect, url_for, session, request, jsonify
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from forms import NameEmailForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "ece444-pra3-secret-key"

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route("/", methods=["GET", "POST"])
def index():
    form = NameEmailForm()

    if form.validate_on_submit():
        session["name"] = form.name.data
        session["email"] = form.email.data
        return redirect(url_for("chat_page"))

    return render_template(
        "index.html",
        form=form,
        current_time=datetime.utcnow()
    )

@app.route("/chat")
def chat_page():
    if "name" not in session:
        return redirect(url_for("index"))

    return render_template("chat.html", name=session["name"])

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"].strip()
    message_lower = message.lower()

    if message_lower.startswith("my name is "):
        chat_name = message[11:].strip().rstrip(".!?")
        session["chat_name"] = chat_name
        reply = f"Nice to meet you, {chat_name}!"

    elif "what is my name" in message_lower:
        if "chat_name" in session:
            reply = f"Your name is {session['chat_name']}."
        else:
            reply = "I do not know your name yet."

    elif "hello" in message_lower:
        reply = "Hello!"

    else:
        reply = "I don't understand."

    return jsonify(reply=reply)

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)