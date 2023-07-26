from flask import Flask, render_template, request, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Siva',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 1, 2023'
    },
    {
        'author': 'Kumar',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 2, 2023'
    },
    {
        'author': 'Raju',
        'title': 'Blog post 3',
        'content': 'third post content',
        'date_posted': 'April 3, 2023'
    },

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        return 








if __name__ == '__main__':
    app.run(debug=True)
