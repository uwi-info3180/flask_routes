"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, jsonify


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')        # You can attach multiple routes to a single function
@app.route('/about/<name>')
def about(name="Mary Jane"):
    """Render the website's about page."""
    return render_template('about.html', name = name)

# Now we can specify routes that accept specific types of data in routes.
# In this case we are saying the parameters must be an 'int'
# Other converters could be 'string', 'float', 'path', etc.
# See http://flask.pocoo.org/docs/0.12/quickstart/#variable-rules
@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    result = str(a + b)
    return render_template('answer.html', answer = result)

@app.route('/add-floats/<float:a>/<float:b>')
def add_floats(a, b):
    result = str(a + b)
    return render_template('answer.html', answer = result)

# You can also make different things happen depending on what HTTP method is used.
# For example, a GET request could retrieve the HTML page, but a POST request
# could send/retrieve a JSON representation of the data returned.
@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id = 1):
    post = {
        "post_id": 1,
        "username": "jseinfeld",
        "title": "The Quick brown fox jumps over the lazy dog",
        "body": "This is the body of the post. Lorem ipsum dolor sit amet.",
        "date": "2017-01-16"
    }

    # If a post request is sent it should return a JSON string.
    if request.method == 'POST':
        return jsonify(post)

    # If it's not a POST request then just display the HTML page.
    return render_template('post.html', post = post)


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
