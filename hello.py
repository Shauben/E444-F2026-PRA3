from datetime import datetime
from flask import Flask, render_template
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
    name = None
    email = None

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

    return render_template(
        "index.html",
        form=form,
        name=name,
        email=email,
        current_time=datetime.utcnow()
    )

@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello, {name}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)