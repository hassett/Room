from qhue import Bridge
import time
import os
import schedule
import datetime

'''
SCHEDULE FUNCTION WORKS
    Implement for morning wake up
    Implement for shower timer

Color:
    1000 -> Red
    6000 -> Orange
    10000 -> Yellow
    20000 -> Green
    40000 -> Blue
    60000 -> Pink

'''


class Hue():

    def __init__(self):
        self.BLUE = 38000
        self.RED = 1000
        self.YELLOW = 8000

    user = User()

    hue = Bridge(user.loc, user.username)

    lights = hue.lights

    ov_lamp = hue.lights[5]
    read_lamp = hue.lights[4]
    bath_light_left = hue.lights[3]
    bath_light_right = hue.lights[2]
    kate = hue.light[8]

    def morning(self):
        a = 0
        while(a is 0):
            dt = datetime.datetime.now()
            if(dt.hour is 5):
                if(dt.minute is 37):
                    hue.morse('wake up right now and win the day')
                    hue.all_on(1)
                    print('Good Morning Sir')
                    break
                time.sleep(29)
            time.sleep(59*60)


    def bath_on(self):
        self.bath_light_left.state(on = True, bri = 250)
        self.bath_light_right.state(on = True, bri = 250)

    def bath_off(self):
        self.bath_light_left.state(on = False)
        self.bath_light_right.state(on = False)

    morse_code = {'a': [0, 1], 'b': [1, 0, 0, 0], 'c': [1, 0, 1],
                'd': [1, 0, 0], 'e': [0], 'f': [0, 0, 1, 0], 'g': [1, 1, 0],
                'h': [0, 0, 0, 0], 'i': [0, 0], 'j': [0, 1, 1, 1],
                'k': [1, 0, 1], 'l': [0, 1, 0, 0], 'm': [1, 1],
                'n': [1, 0], 'o': [1, 1, 1], 'p': [0, 1, 1, 0],
                'q': [1, 1, 0, 1], 'r': [0, 1, 0], 's': [0, 0, 0],
                't': [1], 'u': [0, 0, 1], 'v': [0, 0, 0, 1],
                'w': [0, 1, 1], 'x': [1, 0, 0, 1], 'y': [1, 0, 1, 1],
                'z': [1, 1, 0, 0]}

    def morse_text(self, text):
        text = text.lower()
        text_final = []
        for i in range(len(text)):
            y = self.morse_code[text[i]]
            y.append(2)
            text_final.append(y)
        return(text_final)

    def morse(self, text):
        morse_text = self.morse_text(text)
        morse = []
        for i in morse_text:
            for k in i:
                morse.append(k)
        print(morse)
        counter = 0
        for i in morse:
            if morse[counter] is 0:
                self.all_on(0)
                self.all_off(.5)
            if morse[counter] is 1:
                self.all_on(0)
                self.all_off(1)
            if morse[counter] is 2:
                time.sleep(1.5)
            counter += 1

    def sleep(self):
        os.system("osascript -e 'tell application \"Finder\" to sleep'")

    def all_off(self, timer):
        time.sleep(timer)
        self.ov_lamp.state(on = False)
        self.read_lamp.state(on = False)

    def color_change(self, color):
        self.ov_lamp.state(on = True, bri = 250, hue = color)

    def pulse(self, timer):
        for i in range(timer):
            counter = 0
            for i in range(600):
                self.color_change(counter)
                counter += 100
            countee = 60000
            for i in range(600):
                self.color_change(countee)
                countee -= 100

    def pulse_6(self, timer):
        self.read_lamp.state(on = True, bri = 250)
        for i in range(timer):
            self.color_change(1000)
            self.color_change(6000)
            self.color_change(10000)
            self.color_change(20000)
            self.color_change(40000)
            self.color_change(60000)
            self.color_change(40000)
            self.color_change(10000)
            self.color_change(6000)


    def night(self, read = False):
        print('Good Night Sir')
        self.ov_lamp.state(on = True)
        if(read == True):
            time.sleep(600)
        time.sleep(30)
        self.all_on(1)
        self.all_off(.2)
        self.all_on(2)
        time.sleep(10)
        self.all_off(1)
        self.morning()

    def all_on(self, timer):
        time.sleep(timer)
        self.ov_lamp.state(on = True, bri = 240)
        self.read_lamp.state(on = True, bri = 240)

    def ov_on(self, timer):
        time.sleep(timer)
        self.ov_lamp.state(on = True, bri = 240)

    def read_on(self, timer):
        time.sleep(timer)
        self.read_lamp.state(on = True, bri = 240)

    def ov_off(self, timer):
        time.sleep(timer)
        self.ov_lamp.state(on = False)

    def read_off(self, timer):
        time.sleep(timer)
        self.read_lamp.state(on = False)

    def flash(self, num, timer, wait):
        time.sleep(wait)
        for i in range(num):
            self.all_on(timer)
            self.all_off(timer)
        time.sleep(timer)
        self.all_on(0)

    def dim_no_off(self, timer):
        counter = 240

        for i in range(counter):
            time.sleep(.01)
            self.ov_lamp.state(bri = counter)
            self.read_lamp.state(bri = counter)
            counter -= 1

    def dim_to_off(self, timer):
        counter = 240
        timer = timer / counter

        for i in range(counter):
            time.sleep(timer)
            self.ov_lamp.state(bri = counter)
            self.read_lamp.state(bri = counter)
            counter -= 1
        self.ov_lamp.state(on = False)
        self.read_lamp.state(on = False)

    def kate_on(self, timer):
        self.kate.state(on = True)
hue = Hue()
hue.bath_off()
'''
schedule.every().day.at("21:55").do(hue.all_off, .2)

while True:
    schedule.run_pending()
    time.sleep(60)
'''
