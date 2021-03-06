from __future__ import print_function
from __future__ import division
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import time
import copy
import math
import random
import numpy
from array import array
import datetime
from psychopy import prefs
prefs.general['audioLib'] = ['pygame']
from psychopy import visual,core,data,event,gui
from psychopy import sound
from psychopy.constants import *  # things like STARTED, FINISHED
import csv
from psychopy.visual import ShapeStim
#
#
#
#
#
#
#
# Last updated on: 14/03/2020
#
#
#
#
#
#
#
#
#

########################################################################################
# Draw a box to get experiment and participant information
########################################################################################
expName = u'zsb_task'  # Name the experiment
expInfo = {u'Session': u'001', u'Participant': u'001'} # What the box should ask for
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName) # Draw the bloody box!
if dlg.OK == False: core.quit() # If "cancel" is clicked end the whole thing
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
########################################################################################
########################################################################################


########################################################################################
# Where To Write File
########################################################################################
# Setup files for saving
if not os.path.isdir('ZSB_results'): # Create this folder wherever this script is saved
    os.makedirs('ZSB_results')  # If this fails (e.g. permissions) we will get error
filename = 'ZSB_Experiment_' + '%s_%s' %(expInfo['Participant'], expInfo['date'])+'.txt'
print('filename used for data is ' +filename)
########################################################################################
########################################################################################


########################################################################################
# Define the window
########################################################################################
# Setup the Window
win = visual.Window(fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='grey', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='cm')
########################################################################################
########################################################################################



########################################################################################
# Changeable experimental parameters
########################################################################################
# Text size:
textsize = 0.75
# Fixation cross:
fcross = visual.TextStim(win, text="+")
#########################################################################################



########################################################################################
# Text:
########################################################################################
# Task Instructions:
intro_texti = ''' Task instructions at the start of the experiment. For now, the following trial is an experimental trial. Press any key.  '''
intro_text = visual.TextStim(win, text=intro_texti,pos=(0.0, 0.0), height=textsize,wrapWidth=40,alignHoriz = 'center')
# More task Instructions:
contin_texti = ''' Press the 'space bar' to continue...  '''
contin_text = visual.TextStim(win, text=contin_texti,pos=(0.0, -10), height=textsize,wrapWidth=40,alignHoriz = 'center')
# Your fund title:
y_fundi = '''YOUR FUND'''
y_fund = visual.TextStim(win, text=y_fundi,pos=(-14, 11.5), height=1.6, wrapWidth=40,alignHoriz = 'center')
# Neighbour fund title:
c_fundi = '''COMPETING FUND'''
c_fund = visual.TextStim(win, text=c_fundi,pos=(13.5, 11.5), height=1.6, wrapWidth=40,alignHoriz = 'center')
# Your market performance text:
y_fi = '''Market Performance'''
y_f = visual.TextStim(win, text=y_fi,pos=(14, 3), height=textsize, wrapWidth=40,alignHoriz = 'center')
# Neighbour market performance text:
n_fi = '''Market Performance'''
n_f = visual.TextStim(win, text=n_fi,pos=(-14, 3), height=textsize, wrapWidth=40,alignHoriz = 'center')
# Your fund performance text:
y_fpi = '''Fund Performance'''
y_fp = visual.TextStim(win, text=y_fpi,pos=(14, -4), height=textsize, wrapWidth=40,alignHoriz = 'center')
# Neighbour fund performance text:
n_fpi = '''Fund Performance'''
n_fp = visual.TextStim(win, text=n_fpi,pos=(-14, -4), height=textsize, wrapWidth=40,alignHoriz = 'center')
# Your fund performance PROFIT:
y_fund_profi = '''PROFIT'''
y_fund_prof = visual.TextStim(win, text=y_fund_profi,pos=(14, -2), height=1.5, wrapWidth=40,alignHoriz = 'center',color='green')
# Neighbour fund performance PROFIT:
n_fund_profi = '''PROFIT'''
n_fund_prof = visual.TextStim(win, text=n_fund_profi,pos=(-14, -2), height=1.5, wrapWidth=40,alignHoriz = 'center',color='green')
# Your fund performance LOSS:
y_fund_lossi = '''LOSS'''
y_fund_loss = visual.TextStim(win, text=y_fund_lossi,pos=(14, -2), height=1.5, wrapWidth=40,alignHoriz = 'center',color='red')
# Neighbour fund performance LOSS:
n_fund_lossi = '''LOSS'''
n_fund_loss = visual.TextStim(win, text=n_fund_lossi,pos=(-14, -2), height=1.5, wrapWidth=40,alignHoriz = 'center',color='red')
########################################################################################


########################################################################################
# Response Promts:
########################################################################################
# A key:
a_keyi = '''"A" = Investors Gained'''
a_key = visual.TextStim(win, text=a_keyi,pos=(-14, -9), height=textsize, wrapWidth=40,alignHoriz = 'center')
# S key:
s_keyi = '''"S" = Investors Lost'''
s_key = visual.TextStim(win, text=s_keyi,pos=(-14.5, -10), height=textsize, wrapWidth=40,alignHoriz = 'center')
# K key:
k_keyi = '''"K" = Investors Gained'''
k_key = visual.TextStim(win, text=k_keyi,pos=(14, -9), height=textsize, wrapWidth=40,alignHoriz = 'center')
# L key:
l_keyi = '''"L" = Investors Lost'''
l_key = visual.TextStim(win, text=l_keyi,pos=(13.5, -10), height=textsize, wrapWidth=40,alignHoriz = 'center')
########################################################################################
########################################################################################


########################################################################################
# Define trial types:
########################################################################################
# Experimental trials array
expt_trial_type = []
for n in range(15): # 240 experimental trials in total
    expt_trial_type.append(1)
    expt_trial_type.append(2)
    expt_trial_type.append(3)
    expt_trial_type.append(4)
    expt_trial_type.append(5)
    expt_trial_type.append(6)
    expt_trial_type.append(7)
    expt_trial_type.append(8)
    expt_trial_type.append(9)
    expt_trial_type.append(10)
    expt_trial_type.append(11)
    expt_trial_type.append(12)
    expt_trial_type.append(13)
    expt_trial_type.append(14)
    expt_trial_type.append(15)
    expt_trial_type.append(16)

# Shuffle trial order:
np.random.shuffle(expt_trial_type)
########################################################################################
########################################################################################


########################################################################################
# Define the market screens:
########################################################################################
# Define your market screen:
your_fundi = [[(-.2,-.2),(-.2,.2),(.2,.2),(.2,-.2)],[(-.15,-.15),(-.15,.15),(.15,.15),(.15,-.15)]]
your_fund = ShapeStim(win, vertices=your_fundi, fillColor='white', lineWidth=0, size=16, pos=(-14, 7))
# Define neighbour market screen:
n_fundi = [[(-.2,-.2),(-.2,.2),(.2,.2),(.2,-.2)],[(-.15,-.15),(-.15,.15),(.15,.15),(.15,-.15)]]
n_fund = ShapeStim(win, vertices=n_fundi, fillColor='white', lineWidth=0, size=15, pos=(14, 7))
# Define your market screen PROFIT:
your_fundi_p = [[(-.2,-.2),(-.2,.2),(.2,.2),(.2,-.2)],[(-.15,-.15),(-.15,.15),(.15,.15),(.15,-.15)]]
your_fund_p = ShapeStim(win, vertices=your_fundi_p, fillColor='green', lineWidth=0, size=16, pos=(-14, 7))
# Define neighbour market screen PROFIT:
n_fundi_p = [[(-.2,-.2),(-.2,.2),(.2,.2),(.2,-.2)],[(-.15,-.15),(-.15,.15),(.15,.15),(.15,-.15)]]
n_fund_p = ShapeStim(win, vertices=n_fundi_p, fillColor='green', lineWidth=0, size=15, pos=(14, 7))
# Define your market screen LOSS:
your_fundi_l = [[(-.2,-.2),(-.2,.2),(.2,.2),(.2,-.2)],[(-.15,-.15),(-.15,.15),(.15,.15),(.15,-.15)]]
your_fund_l = ShapeStim(win, vertices=your_fundi_l, fillColor='red', lineWidth=0, size=16, pos=(-14, 7))
# Define neighbour market screen LOSS:
n_fundi_l = [[(-.2,-.2),(-.2,.2),(.2,.2),(.2,-.2)],[(-.15,-.15),(-.15,.15),(.15,.15),(.15,-.15)]]
n_fund_l = ShapeStim(win, vertices=n_fundi_l, fillColor='red', lineWidth=0, size=15, pos=(14, 7))
########################################################################################
########################################################################################

########################################################################################
# Function to show market performance: 
########################################################################################
def show_market(left_market, right_market):
    trial = True
    while trial == True: # while loop to show static market performance grid
        your_fund.draw() # Neutral left market screen
        n_fund.draw() # Neutral right market screen
        y_f.draw()
        n_f.draw()
        left_market_numi = left_market # Identify what number to show for your market
        left_market_num = visual.TextStim(win, text=left_market_numi,pos=(-14, 7), height=textsize, wrapWidth=40,alignHoriz = 'center')
        left_market_num.draw()# Show your market number
        right_market_numi = right_market # Identify what number to show neighbour market
        right_market_num = visual.TextStim(win, text=right_market_numi,pos=(14, 7), height=textsize, wrapWidth=40,alignHoriz = 'center')
        right_market_num.draw()# Show the neighbour market number
        y_fund.draw()
        c_fund.draw()
        win.flip()
        core.wait(0.2) # Keep each market number on screen for x seconds
        break
########################################################################################
########################################################################################


########################################################################################
# Function to show fund performance and que response: 
########################################################################################
def show_fund_res(last_left,last_right,trial_type,response):
    # Determine what the market performance is:
    if trial_type is 1 or trial_type is 2 or trial_type is 3 or trial_type is 4: # LL
        your_fund_l.draw() # left market screen profit/loss
        n_fund_l.draw() # right market screen profit/loss
        y_f.draw() # Your market performance text
        n_f.draw() # Neighbour market performance text
        left_market_numi = last_left # Identify what number to show for your market
        left_market_num = visual.TextStim(win, text=left_market_numi,pos=(-14, 7), height=textsize, wrapWidth=40,alignHoriz = 'center')
        left_market_num.draw()# Show your market number
        right_market_numi = last_right # Identify what number to show neighbour market
        right_market_num = visual.TextStim(win, text=right_market_numi,pos=(14, 7), height=textsize, wrapWidth=40,alignHoriz = 'center')
        right_market_num.draw()# Show the neighbour market number
        y_fund.draw()
        c_fund.draw()
    elif trial_type is 5 or trial_type is 6 or trial_type is 7 or trial_type is 8: # LP
        your_fund_l.draw() # left market screen profit/loss
        n_fund_p.draw() # right market screen profit/loss
        y_f.draw() # Your market performance text
        n_f.draw() # Neighbour market performance text
        left_market_numi = last_left # Identify what number to show for your market
        left_market_num = visual.TextStim(win, text=left_market_numi,pos=(-14, 7), height=textsize, wrapWidth=40,alignHoriz = 'center')
        left_market_num.draw()# Show your market number
        right_market_numi = last_right # Identify what number to show neighbour market
        right_market_num = visual.TextStim(win, text=right_market_numi,pos=(14, 7), height=textsize, wrapWidth=40,alignHoriz = 'center')
        right_market_num.draw()# Show the neighbour market number
        y_fund.draw()
        c_fund.draw()
    elif trial_type is 9 or trial_type is 10 or trial_type is 11 or trial_type is 12: # PL
        your_fund_p.draw() # left market screen profit/loss
        n_fund_l.draw() # right market screen profit/loss
        y_f.draw() # Your market performance text
        n_f.draw() # Neighbour market performance text
        left_market_numi = last_left # Identify what number to show for your market
        left_market_num = visual.TextStim(win, text=left_market_numi,pos=(-14, 7), height=textsize, wrapWidth=40,alignHoriz = 'center')
        left_market_num.draw()# Show your market number
        right_market_numi = last_right # Identify what number to show neighbour market
        right_market_num = visual.TextStim(win, text=right_market_numi,pos=(14, 7), height=textsize, wrapWidth=40,alignHoriz = 'center')
        right_market_num.draw()# Show the neighbour market number
        y_fund.draw()
        c_fund.draw()
    elif trial_type is 13 or trial_type is 14 or trial_type is 15 or trial_type is 16: # PP
        your_fund_p.draw() # left market screen profit/loss
        n_fund_p.draw() # right market screen profit/loss
        y_f.draw() # Your market performance text
        n_f.draw() # Neighbour market performance text
        left_market_numi = last_left # Identify what number to show for your market
        left_market_num = visual.TextStim(win, text=left_market_numi,pos=(-14, 7), height=textsize, wrapWidth=40,alignHoriz = 'center')
        left_market_num.draw()# Show your market number
        right_market_numi = last_right # Identify what number to show neighbour market
        right_market_num = visual.TextStim(win, text=right_market_numi,pos=(14, 7), height=textsize, wrapWidth=40,alignHoriz = 'center')
        right_market_num.draw()# Show the neighbour market number
        y_fund.draw()
        c_fund.draw()
        
        
    # Determine what the fund performance is:
    if trial_type is 1 or trial_type is 5 or trial_type is 9 or trial_type is 13: # LL
        # Fund text:
        y_fp.draw() # Your fund performance text
        n_fp.draw() # Neighbour fund performance text
        y_fund_loss.draw() # Your fund performance text proft/loss
        n_fund_loss.draw() # Neighbour fund performance text profit/loss
    elif trial_type is 2 or trial_type is 6 or trial_type is 10 or trial_type is 14: # PL
        # Fund text:
        y_fp.draw() # Your fund performance text
        n_fp.draw() # Neighbour fund performance text
        y_fund_prof.draw() # Your fund performance text proft/loss
        n_fund_loss.draw() # Neighbour fund performance text profit/loss
    elif trial_type is 3 or trial_type is 7 or trial_type is 11 or trial_type is 15: # LP
        # Fund text:
        y_fp.draw() # Your fund performance text
        n_fp.draw() # Neighbour fund performance text
        y_fund_loss.draw() # Your fund performance text proft/loss
        n_fund_prof.draw() # Neighbour fund performance text profit/loss
    elif trial_type is 4 or trial_type is 8 or trial_type is 12 or trial_type is 16: # PP
        # Fund text:
        y_fp.draw() # Your fund performance text
        n_fp.draw() # Neighbour fund performance text
        y_fund_prof.draw() # Your fund performance text proft/loss
        n_fund_prof.draw() # Neighbour fund performance text profit/loss
            
    # RESPONSE PROMPT:
    # If participant has given no reponses prompt a response for both Qs:
    if response == 0:
        a_key.draw() # Your fund more investors
        s_key.draw() # Your fund less investors
        k_key.draw() # Neighbour fund more investors
        l_key.draw() # Neighbour fund less investors
    # If participant has responded to their Q, prompt to answer next Q:
    else:
        k_key.draw() # Neighbour fund more investors
        l_key.draw() # Neighbour fund less investors
    win.flip()
    
    # If participant has given the first response que and get the second:
    if response == 1:
        keypressed = event.waitKeys(keyList=["j","k","l"])
        if keypressed == ["j"]:
            h=1
        elif keypressed == ["k"]:
            h=1
        elif keypressed == ["l"]:
            h=1
########################################################################################
########################################################################################
    
    
########################################################################################
# Get response function:
########################################################################################
def get_response_1():
    keypressed = event.waitKeys(keyList=["a","s","d"])
    if keypressed == ["a"]:
        show_fund_res(last_left,last_right,expt_trial_type[n],1)
    elif keypressed == ["s"]:
        show_fund_res(last_left,last_right,expt_trial_type[n],1)
    elif keypressed == ["d"]: 
        show_fund_res(last_left,last_right,expt_trial_type[n],1)
########################################################################################
########################################################################################
    
    
########################################################################################
########################################################################################
# Block For Experimental Trials:
########################################################################################
########################################################################################
for n in range(len(expt_trial_type)):
    
    # Create random string of numbers for each market:
    left_market0 = np.random.randint(10,50,15)
    right_market0 = np.random.randint(10,50,15)
    
    # Define last number shown on each market performance:
    last_left = left_market0[-1] # Your fund
    last_right = right_market0[-1] # Neighbour fund
    
    # Section to define what happens on each trial:
    for i in range(15): # Number of trials
        if i == 0:
            intro_text.draw() # intro text
            win.flip()
            keypressed = event.waitKeys(timeStamped=False)
            win.flip()
            core.wait(0.5)
        
        
        # Define what values the left and right market should take:
        left_market = left_market0[i]
        right_market = right_market0[i]
        
        # Call funtion to show market performance:
        show_market(left_market,right_market)
    
    # Call function to show fund performance and que responses:
    show_fund_res(last_left,last_right,expt_trial_type[n],0)
    
    # Call function to get first response:
    get_response_1()
########################################################################################
########################################################################################
