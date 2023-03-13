from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient
client = MongoClient("mongodb+srv://kmanpysev20:0000@cluster0.cknzfkt.mongodb.net/?retryWrites=true&w=majority")
db = client.DOF

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)