## flask app for hello world

from flask import Flask
import numpy as np
import pandas as pd

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello World"



if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
    
    
## host="0.0.0.0",port=5000  it can    from below links
# http://192.168.1.34:5000/
# http://127.0.0.1:5000/
# http://localhost:5000/