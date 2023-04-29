#!/usr/bin/env python3

import sys

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return 'Hello World\n'

if __name__ == '__main__':
    sys.exit(app.run(host='0.0.0.0', port=8080))
