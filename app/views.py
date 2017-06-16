from flask import render_template
from app import models


@app.route('/')
@app.route('/index')
def index():
    return render_template('index')