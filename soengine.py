from flask import Flask
from jinja2 import Environment, PackageLoader
import datetime

app = Flask(__name__)

env = Environment(loader=PackageLoader('standoffish', 'templates'))

homeTemplate = env.get_template("home.html")

@app.route('/0')
def home(currYear = datetime.date.today().year):
    return render_template(home.html, year=currYear);

if __name__ == '__main__':
    app.run()
