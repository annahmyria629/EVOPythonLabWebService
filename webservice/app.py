from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os


port = int(os.getenv("PORT", 5000))
app = Flask(__name__)
app.secret_key = "some secret string"


@app.errorhandler(404)
def page_not_found(e):
    return render_template("not_found.html")


app.register_error_handler(404, page_not_found)


class MyForm(FlaskForm):
    name = StringField('Name and Surname:', validators=[DataRequired()])
    submit = SubmitField(label="Say hello!")


@app.route("/hello/<name>")
def hello(name):
    if "users" in session:
        if name in session.get("users"):
            return render_template("hello.html", greeting="We have already greeted", items=session.get("users"))
        else:
            tmp = session.get("users")
            tmp.append(name)
            session["users"] = tmp
            return render_template("hello.html", greeting=f"Hello {name}", items=session.get("users"))
    else:
        session["users"] = [name]
        return render_template("hello.html", greeting=f"Hello {name}", items=session.get("users"))


@app.route("/", methods=["GET", "POST"])
def index():
    form = MyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            f = form
            return redirect(url_for('hello', name=form.data["name"]))
    return render_template("index.html", form=form)


@app.route("/all_users")
def all_users():
    all_u = session.get("users")
    return render_template("all_users.html", all_users=all_u)


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
