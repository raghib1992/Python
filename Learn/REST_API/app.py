from flask import Flask

app = Flask(__name__)

@app.route('/') # 'http://google.com/'
def home():
    return "Hello Raghib"

app.run(port=5000)