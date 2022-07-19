from flask import Flask, render_template, request, redirect, url_for
from dotenv import dotenv_values

from api.base import blueprint as api

app = Flask(__name__, template_folder="template")
app.register_blueprint(api, url_prefix="/api")
app.secret_key = dotenv_values()["SECRET_KEY"]


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
