#!/usr/bin/env python

from flask import Flask
from flask import request, session, redirect, url_for
from flask import render_template, flash

from flaskext.bcrypt import check_password_hash, generate_password_hash

from screenchop.models import *
from screenchop import config
from screenchop.forms import RegistrationForm, LoginForm, AccountForm

from screenchop.sessions import *


def home():
    # Configure S3 Thumbs directory
    s3ThumbsURL = config.S3_THUMBS_URL
    
    # Configure max images to show on front page
    maxPerRow = config.MAX_IMAGES_PER_ROW
    pageIncr = config.HOME_MAX_IMAGES # Amount of images to increment/paginate

    # For registration/login validation
    regForm = RegistrationForm(request.form)
    loginForm = LoginForm(request.form)
    
    # Query user object. Used to check if tag subscriptions exist
    user = User.objects.get(username=session['username'])

    return render_template('main/home.html', s3ThumbsURL=s3ThumbsURL,
                        maxPerRow=maxPerRow, regForm=regForm, loginForm=loginForm,
                        pageIncr=pageIncr, user=user)
                        
def home_top():
    # Configure S3 Thumbs directory
    s3ThumbsURL = config.S3_THUMBS_URL

    # Configure max images to show on front page
    maxPerRow = config.MAX_IMAGES_PER_ROW
    pageIncr = config.HOME_MAX_IMAGES # Amount of images to increment/paginate

    # For registration/login validation
    regForm = RegistrationForm(request.form)
    loginForm = LoginForm(request.form)
    
    # Query user object. Used to check if tag subscriptions exist
    user = User.objects.get(username=session['username'])
    
    timerange = request.args.get('t', '7d')

    return render_template('main/home_top.html', s3ThumbsURL=s3ThumbsURL,
                        maxPerRow=maxPerRow, regForm=regForm, loginForm=loginForm,
                        pageIncr=pageIncr, timerange=timerange, user=user)
                        
def home_new():
    # Configure S3 Thumbs directory
    s3ThumbsURL = config.S3_THUMBS_URL

    # Configure max images to show on front page
    maxPerRow = config.MAX_IMAGES_PER_ROW
    pageIncr = config.HOME_MAX_IMAGES # Amount of images to increment/paginate

    # For registration/login validation
    regForm = RegistrationForm(request.form)
    loginForm = LoginForm(request.form)

    # Query user object. Used to check if tag subscriptions exist
    user = User.objects.get(username=session['username'])
    
    return render_template('main/home_new.html', s3ThumbsURL=s3ThumbsURL,
                        maxPerRow=maxPerRow, regForm=regForm, loginForm=loginForm,
                        pageIncr=pageIncr, user=user)
                        
def tags():
    ''' /tags view '''
    
    # Display all tags
    tag = 'all'
    
    # Configure S3 Thumbs directory
    s3ThumbsURL = config.S3_THUMBS_URL

    # Configure max images to show on front page
    maxPerRow = config.MAX_IMAGES_PER_ROW
    pageIncr = config.HOME_MAX_IMAGES # Amount of images to increment/paginate
    
    # For registration/login validation
    regForm = RegistrationForm(request.form)
    loginForm = LoginForm(request.form)
    
    # Query user object. Used to check if tag subscriptions exist
    user = User.objects.get(username=session['username'])
    
    return render_template('main/tags.html', tag=tag, s3ThumbsURL=s3ThumbsURL,
                        maxPerRow=maxPerRow, regForm=regForm, loginForm=loginForm,
                        pageIncr=pageIncr, user=user)
    
def tags_single(tag):
    ''' /tags/<tag> view '''
    
    # Check if any tags queried exist
    tagCount = Tag_freq.objects(tag=tag).count()
    
    # Configure S3 Thumbs directory
    s3ThumbsURL = config.S3_THUMBS_URL

    # Configure max images to show on front page
    maxPerRow = config.MAX_IMAGES_PER_ROW
    pageIncr = config.HOME_MAX_IMAGES # Amount of images to increment/paginate
    
    # For registration/login validation
    regForm = RegistrationForm(request.form)
    loginForm = LoginForm(request.form)
    
    # Query user object. Used to check if tag subscriptions exist
    user = User.objects.get(username=session['username'])
    
    return render_template('main/tags.html', tag=tag, tagCount=tagCount, s3ThumbsURL=s3ThumbsURL,
                        maxPerRow=maxPerRow, regForm=regForm, loginForm=loginForm,
                        pageIncr=pageIncr, user=user)


@requires_auth
def upload():
    '''
    The Upload View
    
    '''

    return render_template('main/upload.html')

