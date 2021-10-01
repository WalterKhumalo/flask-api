from flask import Flask
from flask import jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
   response = {"name": os.getenv('NAME', 'variable not set') }
   return jsonify(response)

if __name__ == "__main__":
   app.run(host='0.0.0.0')
