from qhue import Bridge
import os
import schedule
import time

username = 'Ana0aMYQ8dk-5VtKX6DFzb1DXGGZhARssERRZ2sy'

hue = Bridge('10.0.1.189', username)

lights = hue.lights

light = lights[5]

def job():
    print("I'm working...")

schedule.every().day.at("21:52").do(job)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
