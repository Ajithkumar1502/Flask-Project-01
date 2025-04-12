from flask import Flask # type: ignore # type: ignoe

# Create a Flask application instance
app = Flask(__name__)

# Define a route and view function
@app.route('/')
def home():
    return "Hello, World! This is my first web app."

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Hello, {name}!"
    return render_template('greet.html')

if __name__ == '__main__':
    app.run(debug=True)