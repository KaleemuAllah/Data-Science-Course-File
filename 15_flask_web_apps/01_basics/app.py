from flask import Flask

app = Flask(__name__)  # Create an instance of the Flask class

@app.route("/")   # route() decorator to tell Flask what URL should trigger out
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)   # run the application