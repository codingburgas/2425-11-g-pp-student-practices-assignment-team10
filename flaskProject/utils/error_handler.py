from flask import render_template

def render_error_page(e):
    return render_template("errors/generic_error.html", error_message=str(e)), 500