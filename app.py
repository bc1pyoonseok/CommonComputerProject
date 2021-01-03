import os
import io
from flask import Flask, render_template, request, Response, send_file, jsonify
from queue import Queue, Empty
import threading
import time
from flask import Flask
from flask import request
from primeFactor import PrimeFactor
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     target = os.environ.get('TARGET', 'World')
#     try:
#         num=int(request.args.get('input'))
#         if num==1 or num==0:
#             return "{} has no primeFactor".format(num)
#         elif 0<num and num<=1000000:
#             return 'biggest primeFactor of {} is {}'.format(num,PrimeFactor(num))
#         else:
#             return "input range error input must be range of 0~1000000"
#     except:
#         return 'NO INPUT!!! please give the input by adding  <  ?input={your input} > at the end of url'


# limit input file size under 2MB

# model loading

# request queue setting
requests_queue = Queue()
BATCH_SIZE = 1
CHECK_INTERVAL = 0.1

# static variable

# request handling
def handle_requests_by_batch():
    try:
        while True:
            requests_batch = []
            while not (len(requests_batch) >= BATCH_SIZE):
                try:
                    requests_batch.append(requests_queue.get(timeout=CHECK_INTERVAL))
                except Empty:
                    continue

            batch_outputs = []

            for request in requests_batch:
                if len(request["input"]) == 1:
                    batch_outputs.append(str(PrimeFactor(int(request["input"][0]))))
            for request, output in zip(requests_batch, batch_outputs):
                request["output"] = output

    except Exception as e:
        while not requests_queue.empty():
            requests_queue.get()
        print(e)

threading.Thread(target=handle_requests_by_batch).start()

@app.route("/PrimeFactor/", methods=['GET'])
def PrimeFactorFind():

    # if type != 'short' and type != 'long' :
    #     return jsonify({'error': 'This is the wrong address.'}), 400

    # 큐에 쌓여있을 경우,
    if requests_queue.qsize() > BATCH_SIZE:
        return jsonify({'error': 'Too Many Requests'}), 429

    try:
        args = []
        text=request.args.get('input')

        args.append(str(text))

    except Exception:
        print("Empty Text")
        return Response("fail", status=400)

    req = {
        'input': args
    }
    requests_queue.put(req)

    while 'output' not in req:
        time.sleep(CHECK_INTERVAL)

    return req['output']


@app.route('/healthz')
def health():
    return "ok", 200

@app.route('/')
def main():
    return "ok", 200

if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=80)
