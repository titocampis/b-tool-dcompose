from flask import Flask, render_template, request, jsonify

# Defining the flask app name
app = Flask(__name__)

# Variables
WS_HOST = "0.0.0.0"
WS_PORT = 8080

@app.route('/<string:month>/')
def render_index():
    return render_template('base.html', month=month)

if __name__ == "__main__":
    app.run(host=WS_HOST, port=WS_PORT)
