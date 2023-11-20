from flask import render_template, redirect, request, make_response, flash

@app.route("/")
def index():
    return render_template("/index.html")