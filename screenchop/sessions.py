from flask import Flask
from flask import request, redirect, url_for, session
from flask import render_template

from flaskext.bcrypt import check_password_hash

from screenchop.models import *
from screenchop import config



def login():
    if request.method == 'POST':
        #session['username'] = request.form['username']
        username = request.form['username']
        password = request.form['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            return 'Invalid Username and/or Password.'
        
        if check_password_hash(user.password, password) == True:
            session['username'] = username
        else:
            return 'Invalid Username and/or Password.'
        
        return 'Success'
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('home'))