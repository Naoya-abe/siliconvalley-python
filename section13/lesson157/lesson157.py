# Flask
import sqlite3

from flask import Flask
from flask import g  # 本番では命名をしっかり
from flask import render_template
from flask import request
from flask import Response

# Flaskのクラスを作成
app = Flask(__name__)


def get_db():  # FlaskのDB接続パターン
    # g（グローバル）の__databaseにdbとのコネクションがあれば、そのまま返す
    db = getattr(g, '__database', None)
    # なければ、gの__databaseにdbのコネクションを作成して返す
    if db is None:
        db = g.__database = sqlite3.connect('test_sqlite.db')
    return db

# デコレーターがまだ理解できていない
@app.teardown_appcontext　  # アプリケーションが終了する時に必ず実行する
def close_connection(exception):
    db = getattr(g, '_database', None)
    # dbとのコネクションが存在したら、closeする
    if db is not None:
        db.close()

# TODO DBを使った関数の作成

# landingページでは、hello_world()を実行する
@app.route('/')
def hello_world():
    return 'hello world!'

# 他のページを使用 <引数>URLに入力された値を取り出すことができる
@app.route('/hello')  # usernameがない時に400エラーを返さないように、/hello
@app.route('/hello/<username>')
def hello_world2(username=None):
    # return 'hello world2!! {}'.format(username)  毎回文言を書くのも大変なので、templateを使用する
    return render_template('hello.html', username=username)


# 他のメソッドの呼び出し
@app.route('/post', methods=['POST', 'PUT', 'DELETE'])
def show_post():
    # clientが送ってきたリクエストの情報を返す
    return str(request.values['username'])

# DBとのやりとり(sqlite3)


def main():
    app.debug = True

    # サーバー起動（デフォルトで以下のようになる）
    # app.run(host='127.0.0.1', port=5000)
    app.run()


if __name__ == '__main__':
    main()
