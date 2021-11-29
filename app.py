from flask import Flask
from flask_restx import Api, Resource
from flask_cors import CORS, cross_origin

from Member.login import login
from Market.marketList import MarketList

app = Flask(__name__)  # Flask 앱 생성
CORS(app)

api = Api(  # API 서버로 사용할 수 있게해줌.
    app,
    version='0.1',
    title="Playus API Server",
    description="AIP 사용설명서.",
    terms_url="https://www.shingu.ac.kr/",
    license="신구대학교 IT소프트웨어과 HandFarm API")

api.add_namespace(login, '/logins')
api.add_namespace(MarketList, '/market')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
