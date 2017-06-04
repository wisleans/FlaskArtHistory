"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskArtHistory import app

class links(list):
    """description of class"""
    def add_new_arrival(self, name, url):
        self.append((False, name,url))

linklist = links()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Cathedral of Notre Dame',
        year=datetime.now().year,
    )

@app.route('/history')
def history():
    """Renders the home page."""
    return render_template(
        'history.html',
        title='History of Construction'
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        numbers = [1,2,3,4],
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Cathedral of Notre Dame'
    )

@app.route('/workscited')
def workscited():
    linklist.add_new_arrival("name","url")
    return render_template('workscited.html')