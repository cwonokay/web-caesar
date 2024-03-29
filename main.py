from caesar import rotate_string
from flask import Flask, request


app = Flask(__name__)
app.config['DEBUG'] = True


form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form action ="/" method="POST">
     <label for "rot">Rotate by:</label>
      <input type="text" id="rot" name="rot" value="0">
       <textarea name="text" >{0}</textarea>
        <input type="Submit">
    </form>


      
    </body>
</html>
"""


@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    message = str(request.form['text'])
    encryptText = rotate_string(message, rot)

    return form.format(encryptText)


@app.route("/")
def index():
    return form.format("")


app.run()
