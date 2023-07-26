from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '1c38d3c9307530d378b800c2a1ca63fb'

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


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account Created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Sign-Up',form = form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
           flash(f"you have been logged in!", 'success') 
           return redirect(url_for('home'))
        else:
           flash(f"Incorrect Credentials! Please check username and password", 'danger') 
    return render_template('login.html', title='Login',form = form)




if __name__ == '__main__':
    app.run(debug=True)
