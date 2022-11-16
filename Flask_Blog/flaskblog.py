from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='cfebcdd90ba71f0c3ad5c64b699bbdd7'

posts = [{
           'author':'Audu aliyu',
           'title': 'Blog post 1',
           'content': 'First post content',
           'date_posted': 'April 21, 2018'
           },
           {
           'author':'sodiq akanmu',
           'title': 'Blog post 2',
           'content': 'second post content',
           'date_posted': 'April 21, 2019'
           }
        ]

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about_page():
    return render_template("about.html", title="about")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()()
    return render_template("login.html", title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)