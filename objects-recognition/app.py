# app.py
from flask import Flask
from flask import request
import tf_funcion

app = Flask(__name__)

@app.route("/recognize", methods=["POST"])
def hello():
    content = request.get_json(silent=True)
    return tf_funcion.main(content.src)