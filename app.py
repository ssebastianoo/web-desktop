from flask import Flask, render_template, redirect

app = Flask("")

@app.route("/")
def index():
    return "toast"

app.run("0.0.0.0", port=3000)
