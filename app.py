import os

from flask import Flask
from flask import request
from primeFactor import PrimeFactor
app = Flask(__name__)

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    try:
        num=int(request.args.get('input'))
        if num==1 or num==0:
            return "{} has no primeFactor".format(num)
        elif 0<num and num<=1000000:
            return 'biggest primeFactor of {} is {}'.format(num,PrimeFactor(num))
        else:
            return "input range error input must be range of 0~1000000"
    except:
        return 'NO INPUT!!! please give the input by adding  <  ?input={your input} > at the end of url'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))

