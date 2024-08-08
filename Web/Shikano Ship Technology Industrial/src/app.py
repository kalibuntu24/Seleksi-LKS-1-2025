from flask import Flask, render_template_string, request, send_from_directory
from random import choice
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        return greeting(name)
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>Shikano Ship Technology Industrial</title>
        <style>
            body {
                background-image: url("/background.png");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                font-family: Arial, sans-serif;
            }
            h3 {
                color: white;
                margin-top: 20%;
            }
            form {
                color: white;
            }
        </style>
    </head>
    <body style="text-align: center;">
        <h3>Ahoyyy, Selamat Datang di Kapalku <br> Siapa Namamu Wahai Pengunjung?</h3>
        <form method="post">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" required>
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>''')

def greeting(name):
    greeting = choice(["Hi", "Hello", "Welcome"])
    template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>Shikano Ship Technology Industrial</title>
        <style>
            body {
                background-image: url("/background.png");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                font-family: Arial, sans-serif;
            }
            h3 {
                color: white;
                margin-top: 20%;
            }
            form {
                color: white;
            }
        </style>
    </head>
    <body style="text-align: center;">
        <h3>''' + greeting + ' ' + name + '''!<br>Terima kasih Telah berkunjung di Kapalku</h3>
        <form method="post" action="/">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" required>
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>'''
    return render_template_string(template)

@app.route('/background.png')
def background():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'background.png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
