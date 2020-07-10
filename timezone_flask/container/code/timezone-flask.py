'''
module : module_template.py
version : see module_version variable
Language : Python 3.x
author : andrew christ
email : andrew@openmarmot.com
notes :
'''


#import built in modules
from datetime import datetime
import pytz
from flask import Flask, render_template, request, jsonify, make_response

#import custom packages

# module specific variables
module_version='0.0' #module software version
module_last_update_date='June 07 2020' #date of last update

#global variables

app = Flask(__name__)
 
@app.route('/')
def index():
    response = make_response(getTime())
    response.headers["content-type"] = "text/plain"
    response.headers['Cache-Control'] = "no-store"
    return response
 
def getTime():
    b=[]
    b.append('Current Time : All Timezones')
    b.append(' ')
    format = "%Y-%m-%d %H:%M:%S %Z%z"
    for tz in pytz.all_timezones:
        b.append('--')
        b.append(tz)
        b.append(datetime.now(pytz.timezone(tz)).strftime(format))
#    print(b)
    return str(b).replace(',','\n').replace("'","").replace('[','').replace(']','')
 
if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0')