from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    # return "Hello World"
    # return "<html><body><h1>Hello World</h1></body></html>"
    fname = "Mahdi"
    return render_template("home.html", fname=fname)


@app.route("/contact", methods=["GET"])
def contact_us():
    # print(request.method)
    # print(request.args["submit"])
    # print(len(request.args))
    # return "you may contact us thru email or phone."
    show_form = False
    fname = ""
    if len(request.args) == 0:
        # pass
        show_form = True

    else:
        # pass
        fname = request.args["fname"]
    return render_template("contact.html", show_form=show_form, fname=fname)


# @app.route("/result", methods=["GET"])
# def contact_result():
#     fname = request.args["fname"]
#     email = request.args["email"]
#     description = request.args["description"]
#     return request.args


if __name__ == "__main__":
    app.run(debug=True, port=3033)
