from knust import app
from flask import g, render_template, redirect, url_for, flash, request, make_response
from knust.models import Result, User
from knust.forms import RegisterForm, LoginForm
from knust import db
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from flask_moment import Moment

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              f_name=form.f_name.data,
                              s_name=form.s_name.data,
                              email_address=form.email_address.data,
                              password=form.password1.data,
                              student_id=form.student_id.data,
                              index_no=form.index_no.data,
                              course=form.course.data,
                              contact=form.contact.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully! You are now logged in as {user_to_create.username}', category='success')
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error in creating a user: {err_msg[0]}', category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        attempted_password = form.password.data
        if attempted_user and attempted_user.check_password_correction(attempted_password):
            login_user(attempted_user, form.remember_me.data)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Username or password not found! Please try again', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out", category='info')
    return redirect(url_for('home_page'))

@app.route('/profile')
def profile_page():
    return render_template('profile.html')


@app.route('/courses')
def course_page():
    return render_template('courses.html')

@app.route('/results')
def results_page():
    return render_template('results.html')

@app.route('/fees')
def fees_page():
    return render_template('fees.html')

@app.route('/notifications')
def notification_page():
    date = datetime.now()
    #return date.strftime("%d/%m/%y")
    #return str(date)
    return render_template('notification.html', current_time=datetime.utcnow())

@app.route('/blogs')
def blogs_page():
    return render_template('blog.html')

@app.route('/posts')
def posts_page():
    return render_template('posts.html')

@app.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                'VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

@app.route('/blog')
def blog_page():
    return render_template('blog/blog.html')

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

def get_comment(id, check_author=True):
    if check_author and comment['author_id'] == g.user['id']:
        return comment
    else:
        comment = get_db().execute(
            'SELECT c.id, body, created, author_id, username'
            ' FROM comment c JOIN user u ON c.author_id = u.id'
            ' WHERE c.id = ?',
            (id,)
        ).fetchone()

        if comment is None:
            abort(404, f"Comment id {id} doesn't exist.")

        if check_author and comment['author_id'] != g.user['id']:
            abort(403)

        return comment

@app.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))