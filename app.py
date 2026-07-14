from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello Mava! 🚀Version -2 is successfully deployed in Jenkins Pipeline!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
