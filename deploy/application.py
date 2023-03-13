from flask import Flask, render_template, request, jsonify, send_file, url_for

from pymongo import MongoClient
client = MongoClient("mongodb+srv://kmanpysev20:0000@cluster0.cknzfkt.mongodb.net/?retryWrites=true&w=majority")
db = client.DOF

application = app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

# @app.route('../static/video/<string:videoName>')
# def video(videoName):
#     return send_file("video/"+videoName)

# @app.route('/video/<string:file_name>',methods=['GET','POST'])
# def home(file_name):
#     return render_template("index.html",file_name=file_name)

if __name__ == "__main__":
    app.run()