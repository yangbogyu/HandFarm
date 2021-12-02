from logging import fatal
import os
import pymysql
import json
import datetime
import bcrypt
import jwt
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

login = Namespace(
    name='login',
    description='login API'
)


@login.route('')
class Login(Resource):
    def put(self):
        '''로그인 인증'''

        db = setDB()
        data = request.get_json()
        me_id = data['me_id']
        me_pw = data['me_pw']
        base = db.cursor()
        sql = f'select * from member\
                where me_id = "{me_id}"\
                and me_pw = "{me_pw}"'
        base.execute(sql)
        member = base.fetchall()

        for i in member:
            i['me_joindate'] = str(i['me_joindate'])

        if member:
            return {'login': True,
                'data' : member[0]}
        else:
            return {'login': False}
