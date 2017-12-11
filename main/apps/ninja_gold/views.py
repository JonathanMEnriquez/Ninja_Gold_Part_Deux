# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    try:
        request.session['gold']
    except:
        request.session['gold'] = 0
    try:
        request.session['activities']
    except:
        request.session['activities'] = []
    return render(request, 'ninja_gold/index.html')

def farm(request):
    if request.method == 'POST':
        earnings = random.randint(10,21)
        request.session['gold'] += earnings
        action_dict = {}
        statement = 'You have earned {} gold through hard work on the farm. YASSS!!!'.format(earnings)
        action_dict['statement'] = statement
        action_dict['color'] = 'green'
        temp_list = request.session['activities']
        temp_list.insert(0, action_dict)
        request.session['activities'] = temp_list
        return redirect('/')
    else:
        return redirect('/')

def cave(request):
    if request.method == 'POST':
        earnings = random.randint(5,11)
        request.session['gold'] += earnings
        action_dict = {}
        statement = 'You have earned {} gold through hard work mining the cave. Wowwwwwz!!!'.format(earnings)
        action_dict['statement'] = statement
        action_dict['color'] = 'green'
        temp_list = request.session['activities']
        temp_list.insert(0, action_dict)
        request.session['activities'] = temp_list
        return redirect('/')
    else:
        return redirect('/')

def house(request):
    if request.method == 'POST':
        earnings = random.randint(2,6)
        request.session['gold'] += earnings
        action_dict = {}
        statement = 'You have earned {} gold through hard work at home doing what? I do not know. Cray Cray!!!'.format(earnings)
        action_dict['statement'] = statement
        action_dict['color'] = 'green'
        temp_list = request.session['activities']
        temp_list.insert(0, action_dict)
        request.session['activities'] = temp_list
        return redirect('/')
    else:
        return redirect('/')

def casino(request):
    if request.method == 'POST':
        earnings = random.randint(-50,51)
        request.session['gold'] += earnings
        action_dict = {}
        if earnings > 0:
            statement = 'Luck has been on thy side. You won {} gold at the casino!'.format(earnings)
            action_dict['color'] = 'green'
        elif earnings < 0:
            earnings *= -1
            statement = 'What would your mother say if she found out you lost {} gold gambling your hard-earned money away?'.format(earnings)
            action_dict['color'] = 'red'
        else:
            statement = 'Well...that was some wasted time. You won nothing at the casino. At least you did not lose, amirite?'
            action_dict['color'] = 'none'
        action_dict['statement'] = statement
        temp_list = request.session['activities']
        temp_list.insert(0, action_dict)
        return redirect('/')
    else:
        return redirect('/')