from app import app

# uwsgi 실행파일
if __name__ == '__main__':
    app.run(host='0.0.0.0')