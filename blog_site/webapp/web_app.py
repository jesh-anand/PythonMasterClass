from flask import Flask
from flask import render_template
from flask import request
from flask import session

from blog_site.common.database import Database
from blog_site.webapp.models.user import User

app = Flask(__name__)
app.secret_key = '\x1e\x14\xe6\xa0\xc5\xcc\xd9\x7f\xe5\xe8\x1cZ\xc5\xf2r\xb0W#\xed\xb6\xc8'


@app.route('/')
def home_temmplate():
    return render_template("home.html")


@app.route('/login')
def login_template():
    return render_template("login.html")


@app.route('/register')
def register_template():
    return render_template("register.html")


@app.before_first_request
def init_database():
    Database.initialize()


# TODO: Fix login issue
@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None
        return render_template("login-error.html")

    return render_template("profile.html", email=session['email'])


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email, password)

    return render_template("register-success.html", email=session['email'])


if __name__ == '__main__':
    app.run(port=8660, debug='True')
