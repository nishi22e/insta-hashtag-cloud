from flask import Flask, render_template

app = Flask("Insta Word Cloud")


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
