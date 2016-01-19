from flask import Flask
from flask import *
from jinja2 import Environment, PackageLoader, FileSystemLoader
import flask
import datetime

app = Flask(__name__)

env = Environment(loader=PackageLoader('standoffish'))


@app.route('/')
def root():
    return redirect(url_for('home'))


@app.route('/0')
def home():
    homeTemplate = env.get_template("home.html")
    return render_template ( 
            homeTemplate, 
            year = datetime.date.today().year, 
            css = url_for('static', filename='sobase.css'),
            title = 0 )

if __name__ == '__main__':
    app.run(debug=True)
    
    
