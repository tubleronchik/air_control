# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def getting_data():
    print('data is coming!')

    if(request.method == 'POST'):
        data = request.get_json() #for content with "application/json" headers
        f = open('data.txt', 'a')
        f.write(str(data))
        f.close()
        print(data)
        return jsonify(data)

    else:
        return 'no data'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
