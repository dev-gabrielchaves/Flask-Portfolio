from app import app
from flask import render_template
from app.projects import projects

@app.route('/')
def home():
    return render_template('home.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')