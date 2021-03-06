import os
from flask import Flask, render_template, send_from_directory
import logging
#logging.basicConfig(format = "[%(levelname)s] - %(asctime)s - %(message)s", level=logging.DEBUG, handlers = [logging.StreamHandler(), logging.FileHandler("log.txt")])
#logging.debug("Application started")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True) #debug=True: refreshes page every time a change is made. turned off in production 
    
