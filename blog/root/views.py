from blog.root import root
from flask import render_template, current_app


@root.route('/')
def index():
    return render_template('index.html')
