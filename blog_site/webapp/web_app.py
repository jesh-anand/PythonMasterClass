from flask import Flask
from flask import render_template
from flask import request
from flask import session

from blog_site.webapp.models.user import User

app = Flask(__name__)


@app.route('/')
def hello_method():
    return render_template("login.html")


# TODO: To get the profile page to render email address
@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)

    return render_template("profile.html", email=session["email"])


if __name__ == '__main__':
    app.run(port=8660)
