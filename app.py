from flask import Flask, render_template, request, jsonify, send_file, url_for

from pymongo import MongoClient
client = MongoClient("mongodb+srv://kmanpysev20:0000@cluster0.cknzfkt.mongodb.net/?retryWrites=true&w=majority")
db = client.DOF

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


# Riot API에서 가져올 데이터
riot_url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"

# Riot API Key
riot_api_key = "RGAPI-d426ee2b-294e-4229-85c8-cce19300689c"

@app.route("/userInfo", methods=["POST"])
def userInfo():
    
    account_name = request.form["account_name"]

    # Riot API에서 가져올 데이터
    url = riot_url + account_name

    # requests 모듈을 사용하여 API 요청
    response = request.get(url.format(account_name), headers={"X-Riot-Token": riot_api_key})

    # 요청이 성공하면 JSON 데이터를 반환
    if response.status_code == 200:
        data = response.json()
        print(data)
    else :
        print(response)


    return jsonify({'msg': 'POST 연결 완료!'})
    
@app.route("/bucket", methods=["GET"])
def bucket_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == "__main__":
    app.run(debug=True, port=5000)