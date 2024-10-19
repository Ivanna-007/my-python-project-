from flask import Flask, render_template
import os

app = flask (__name__)




@app.route ('/')
def index():
    return render_template ('index')


if __name__ == '__main__':
    app.run(debug=True)