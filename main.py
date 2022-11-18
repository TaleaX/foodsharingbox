from flask import Flask, render_template
import os

app = Flask(__name__)
img_path = os.path.join('static', 'image.jpg')
style_path = os.path.join('static', 'style.css')

@app.route("/")
def home():
    return render_template("index.html", user_image = img, style = style_path)

if __name__ == "__main__":
    #make_picture()
    app.run()
