from crypt import methods
# from curses import flash
from flask import render_template,flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect( url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Miguel' , 'sex':'male'}
    posts = [
        {
            'author' : {'username': 'John'},
            'body' : 'Beautiful day in Portland!'
        },
        {
            'author' : {'username' : 'Susan'},
            'body' : 'The Avengers movie was so cool!'
        }
        # ,
        # {
        #     'author' : {'username' : 'Stacy'},
        #     'body' : 'The soul will folow the way!'
        # },
        # {
        #     'author' : {'username' : 'Susan'},
        #     'body' : "I wan't go to Canada!"
        # },
        # {
        #     'author' : {'username' : 'John'},
        #     'body' : 'Even don\'t think about it!'
        # }
    ]

    return render_template('index.html' ,title= 'test', user=user,posts=posts)