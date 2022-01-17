from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp
import os
from webservice.config import Config
from webservice.db import Base, Users
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config.from_object(Config)

engine = create_engine(app.config["DATABASE_URI"])
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
db_session = DBSession()


@app.errorhandler(404)
def page_not_found(e):
    return render_template("not_found.html")


app.register_error_handler(404, page_not_found)


class MyForm(FlaskForm):
    name = StringField('Name and Surname:', validators=[DataRequired(),
                                                        Regexp("^[a-zA-Z]+$",
                                                               message="Field must contain only letters")],
                       render_kw={"onfocus": "this.value=''; document.querySelector('span').hidden = true;"})
    submit = SubmitField(label="Say hello!")


@app.route("/hello/<name>")
def hello(name):
    app.logger.warning(request.url)
    user = db_session.query(Users).filter_by(name=name).all()
    if user:
        return render_template("hello.html", greeting="We have already greeted")
    else:
        db_session.add(Users(name=name))
        db_session.commit()
        return render_template("hello.html", greeting=f"Hello, {name}")


@app.route("/", methods=["GET", "POST"])
def index():
    app.logger.warning(request.url)
    form = MyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            return redirect(url_for('hello', name=form.data["name"]))
    return render_template("index.html", form=form)


@app.route("/all_users")
def all_users():
    app.logger.warning(request.url)
    all_u = db_session.query(Users).all()
    return render_template("all_users.html", all_users=all_u)


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
