from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content="Testing")
    # return render_template("index.html", content="Testing", x=4)
    # return render_template("index.html", content={"a":2, "b":"hello"})

if __name__ == "__main__":
    app.run()