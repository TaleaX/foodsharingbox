#!/usr/bin/env python3

from flask import Flask, render_template
from flask import Flask, url_for
from flask_cache_buster import CacheBuster

app = Flask(__name__)


config = {
     'extensions': ['.jpg', '.css'],
     'hash_size': 10
}

cache_buster = CacheBuster(config=config)
cache_buster.register_cache_buster(app)

@app.route("/")
def home():
    img_path = url_for('static', filename='image.jpg')
    style_path = url_for('static', filename='style.css')
    return render_template("index.html", user_image = img_path, style = style_path)

if __name__ == "__main__":
    app.run()
