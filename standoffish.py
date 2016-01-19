from flask import Flask
from flask import *
from jinja2 import Environment, PackageLoader, FileSystemLoader
import datetime

app = Flask(__name__)

env = Environment(loader=PackageLoader('standoffish'))

baseTemplate = env.get_template('base.html')


@app.route('/')
def root():
    return redirect(url_for('home'))

@app.route('/0')
def home():
    post = render_template('content/2016-01-18.html')
    year = datetime.date.today().year
    css = url_for('static', filename='sobase.css')
    title = 0 
    
    return render_template ([baseTemplate, year, css, title, post])

@app.route('/photography')
def photography():
    galleryTemplate = env.get_template('gallery.html')
    

if __name__ == '__main__':
    app.run(debug=True)
    
    
