from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    products = ["Pão Frances", "Bagguete", "Pretzel"]
    return products[1]