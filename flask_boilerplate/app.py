from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', 
                           title="Welcome to My Flask App", 
                           heading="Hello, World!", 
                           message="This is a simple Flask application using Jinja2 templates.",
                           items=['Item 1', 'Item 2', 'Item 3'])

if __name__ == '__main__':
    app.run(port=8181)
