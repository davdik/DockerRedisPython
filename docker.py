import time

import redis
from flask import Flask

app = Flask(__name__)

@app.route('/')
def score():
    file = open("C:\Temp\MemoryScore.txt", "r")
    print(file.read())
    return file
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)