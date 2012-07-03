#!/usr/bin/env python

from flask import Flask
from flask import request, session, redirect, url_for
from flask import render_template, flash

from screenchop.models import *
from screenchop import config
from screenchop.forms import RegistrationForm, LoginForm

from screenchop.sessions import *

app = Flask(__name__)

def chop(filename):
    '''
    The Chop View
    
    '''
    chop = Post.objects.get(filename = filename)
    vote = Vote.objects(username=session['username'], postuid=chop.uid)
    for v in vote:
        print 'Upvoted: ', v.upvoted
        print 'Downvoted: ', v.downvoted
    
    # For registration/login validation
    regForm = RegistrationForm(request.form)
    loginForm = LoginForm(request.form)
    
    fullURL = config.DOMAIN_URL
    shortURL = config.SHORT_DOMAIN_URL
    
    score = int(chop.upvotes) - int(chop.downvotes)
    print 'upvotes: ', chop.upvotes
    print 'downvotes: ', chop.downvotes
    print 'score: ', score
        
    return render_template('chops/chop.html', chop=chop, regForm=regForm,
                            loginForm=loginForm, fullURL=fullURL,
                            shortURL=shortURL, score=score, vote=vote)

