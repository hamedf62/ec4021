from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///flask_db.db", echo=False)

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contact"
    id = Column(Integer, primary_key=True)
    fname = Column(String)
    email = Column(String)
    description = Column(String)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# add test record to database
# session.add(Contact(fname="hasan", email="hasan@yahoo.com", description="nothing"))
# session.commit()


# create the flask app
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
        show_form = True

    else:
        fname = request.args["fname"]
        email = request.args["email"]
        description = request.args["description"]

        session.add(Contact(fname=fname, email=email, description=description))
        session.commit()

    return render_template("contact.html", show_form=show_form, fname=fname)


if __name__ == "__main__":
    app.run(debug=True, port=3033)
