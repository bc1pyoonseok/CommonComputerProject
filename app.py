import os

from flask import Flask
from flask import request
from primeFactor import PrimeFactor
app = Flask(__name__)

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    num=int(request.args.get('input',-1))
    if num==-1:
        return 'NO INPUT!!! please give the input by adding  <  ?input={your input} > at the end of url'
    if num==1:
        return "1 has no primeFactor"
    if num>1000000:
        return "input range error"
    return 'Hello your answer is {}!\n'.format(PrimeFactor(num))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))

