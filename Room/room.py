from hue import Hue
from easygui import msgbox
from flask import Flask, jsonify, request
from django.http import HttpResponse

hue = Hue()

sector = input('Where do you want to change? ').lower()
if(sector == 'night'):
    hue.night()

action = input('What do you want to do? ')
action = action.lower()
if(action != 'flash' and action != 'morse'):
    timer = float(input('How long of a wait? '))

if(action == 'all on'):
    hue.all_on(timer)
if(action == 'all off'):
    hue.all_off(timer)
if(action == 'flash'):
    timer = float(input('How long to you want between flashes? '))
    number = int(input('How many times do you want a flash? '))
    wait = float(input('How long to you want to wait? '))
    hue.flash(number, timer, wait)
if(action == 'lamp on' or action == 'read on'):
    hue.read_off(timer)
if(action == 'lamp off' or action == 'read off'):
    hue.read_off(timer)
if(action == 'top off'):
    hue.ov_off(timer)
if(action == 'top on'):
    hue.ov_on(timer)
if(action == 'morse' or action == 'morse code'):
    text = input('What would you like to say? ')
    text = text.replace(' ','')
    hue.morse(text)
if(action == 'color change' or action == 'change color'):
    color = int(input('What color? '))
    hue.color_change(color)
if(action == 'kate'):
    hue.kate_on(timer)

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main():
    return HttpResponse("<center>Welcome</center>"), 200

'''
DEBUGGING...

1. Lamp/Read doesn't seem to respond when called individually


TODO (for pi)...

1. Get username for that computer (just call create_username from qhue)

DEBUGGED

1. Morse code only outputting 0s
    a. Added a counter instead of the for loop variable and the problem
    seemed to be fixed

'''
