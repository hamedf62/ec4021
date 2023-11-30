from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    # return "Hello World"
    # return "<html><body><h1>Hello World</h1></body></html>"
    fname = "Mahdi"
    return render_template("hello.html", fname=fname)


@app.route("/contact")
def contact_us():
    return "you may contact us thru email or phone."


if __name__ == "__main__":
    app.run(debug=True)
