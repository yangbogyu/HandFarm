from logging import fatal
import os
import pymysql
import json
import datetime
from flask import request
from flask_restx import Resource, Api, Namespace
from dotenv import load_dotenv

load_dotenv()  # `.env`파일 불러옴

def setDB(): # db연동
    db = pymysql.connect(host=os.getenv('MYSQL_HOST'),
                    port=int(os.getenv('MYSQL_PORT')),
                    user=os.getenv('MYSQL_USER'),
                    passwd=os.getenv('MYSQL_PASSWORD'),
                    db=os.getenv('MYSQL_DATABASE'),
                    charset=os.getenv('MYSQL_CHARSET'),
                    cursorclass=pymysql.cursors.DictCursor)
    return db

MarketList = Namespace(
    name='MarketList',
    description='MarketList API'
)


@MarketList.route('')
class Search(Resource):
    def get(self):
        '''마켓 메인'''
        db = setDB()

        base = db.cursor()
        sql = f'select * from product'

        base.execute(sql)
        market = base.fetchall()

        for i in market: # 날짜 데이터 문자열 변환
            i['product_redate'] = str(i['product_redate'])

        return { 'market' : market}

