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
    css = url_for('static', filename='sobase.css')
    post = [] 
    return render_template (
                    baseTemplate,
                    post = post,
                    year = datetime.date.today().year,
                    css = css,
                    title = 0
                    )
 

@app.route('/photography')
def photography():
    galleryTemplate = env.get_template('gallery.html')

def getPost():
    

    return "finish this function"
    

if __name__ == '__main__':
    app.run(debug=True)
    
    
