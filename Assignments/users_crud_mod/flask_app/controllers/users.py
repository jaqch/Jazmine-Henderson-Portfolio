from flask_app import app
from flask import Flask, render_template, request, redirect, session
from flask_app.models.user import User

@app.route("/users")
def index():
    users = User.get_all()
    return render_template("read_all.html", all_users=users)


@app.route('/users/new')
def user_submission():
    return render_template("create.html")

@app.route('/users/processing/', methods=['POST'])
def create_user():
    User.save(request.form)
    id = User.get_max_id()[0]["MAX(id)"]
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>')
def show_user(id):
    user=User.get_single_user(id)
    return render_template("read_one.html",current_user=user)

@app.route('/users/<int:id>/edit')   
def edit_user(id):
    user= User.get_single_user(id)
    return render_template("edit_user.html",current_user=user)    

@app.route('/users/update/<int:id>',methods=['POST'])
def update(id):
    User.update(request.form, id)
    return redirect(f'/users/{id}')


@app.route('/users/<int:id>/destroy')
def delet(id):
    User.delet(id)
    return redirect('/users')