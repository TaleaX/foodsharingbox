from flask import Flask, render_template
from flask import Flask, url_for
from flask_cache_buster import CacheBuster
import os

app = Flask(__name__)

config = {
     'extensions': ['.jpg', '.css', '.csv'],
     'hash_size': 10
}

cache_buster = CacheBuster(config=config)
cache_buster.register_cache_buster(app)

@app.route("/")
def home():
    return render_template("index.html", user_image = url_for('static', filename='image.jpg'), style = url_for('static', filename='style.css'))

if __name__ == "__main__":
    #make_picture()
    app.run()
