import os
import time
import sys
import Adafruit_DHT as dht
import datetime

from flask import Flask, render_template, url_for
app = Flask(__name__)

h,t=dht.read_retry(dht.DHT11, 17)
temp = t
hum = h
#temp = 5
#hum = 99
@app.route("/")
def hello():
   templateData = {
      'temp' : temp,                                        
      'hum' : hum
   }
   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
