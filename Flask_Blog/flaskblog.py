from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)