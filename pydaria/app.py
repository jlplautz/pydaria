from flask import Flask, render_template
from flask_bootstrap import Bootstrap



app = Flask(__name__)

app.config['TITLE'] = 'Pydaria'
Bootstrap(app)

@app.route('/')
def index():
    products = ["Pão Frances", "Bagguete", "Pretzel"]
    return render_template('index.html', products=products)
