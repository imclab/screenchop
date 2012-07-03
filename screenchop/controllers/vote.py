#!/usr/bin/env python

'''
vote.py - Controller to upvote and downvote posts/chops.

'''
import os, sys
from time import strftime

from flask import Flask
from flask import request, session


from screenchop import config
from screenchop.sessions import requires_auth
from screenchop.models import Post, Vote

app = Flask(__name__)

def upvote():
    chop = request.form['chop']
    chopObject = Post.objects.get(filename=chop)
    vote, created = Vote.objects.get_or_create(username=session['username'], postuid=chopObject.uid)
    
    if created:
        Post.objects(filename=chop).update_one(inc__upvotes=1)
        Vote.objects(username=session['username'],
                postuid=chopObject.uid).update_one(set__upvoted=True,
                                                    set__downvoted=False)
        return 'upvoted'
        
    elif vote.upvoted == False and vote.downvoted == True:
        Post.objects(filename=chop).update_one(inc__upvotes=1, dec__downvotes=1)
        Vote.objects(username=session['username'],
                postuid=chopObject.uid).update_one(set__upvoted=True,
                                                    set__downvoted=False)
        return 'upvoted2'
        
    else:
        Vote.objects(username=session['username'],
                        postuid=chopObject.uid).update_one(set__upvoted=True,
                                                            set__downvoted=False)
        return 'changed to upvote'

    print 'Upvoted: ', vote.upvoted
    print 'Downvoted: ', vote.downvoted

    
def downvote():
    chop = request.form['chop']
    chopObject = Post.objects.get(filename=chop)
    vote, created = Vote.objects.get_or_create(username=session['username'], postuid=chopObject.uid)
    
    if created:
        Post.objects(filename=chop).update_one(inc__downvotes=1)
        Vote.objects(username=session['username'],
                postuid=chopObject.uid).update_one(set__upvoted=False,
                                                    set__downvoted=True)
        return 'downvoted'
        
    elif vote.downvoted == False and vote.upvoted == True:
        Post.objects(filename=chop).update_one(inc__downvotes=1, dec__upvotes=1)
        Vote.objects(username=session['username'],
                postuid=chopObject.uid).update_one(set__upvoted=False,
                                                    set__downvoted=True)
        return 'downvoted2'
        
    else:
        Vote.objects(username=session['username'],
                        postuid=chopObject.uid).update_one(set__upvoted=False,
                                                            set__downvoted=True)
        return 'changed to downvote'

    print 'Upvoted: ', vote.upvoted
    print 'Downvoted: ', vote.downvoted

