#package
from flask import Blueprint, redirect, render_template, request, flash, url_for

#project
from car_inventory.forms import UserLoginForm
from car_inventory.models import User, db

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup',methods=['GET','POST'])
def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email,password)

            user = User(email, password = password)
            db.session.add(user)
            db.session.commit()

            flash(f'You have created an account for {email}.','user-created')
            return redirect(url_for('auth.signin'))

    except:
        raise Exception('Invalid Form Data: Please check your form.')

    return render_template('signup.html', form=form)

@auth.route('/signin',methods=['GET','POST'])
def signin():
    form = UserLoginForm()
    return render_template('signin.html',form=form)

