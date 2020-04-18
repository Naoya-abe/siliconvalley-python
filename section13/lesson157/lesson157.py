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
# アプリケーションが終了する時に必ず実行する
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    # dbとのコネクションが存在したら、closeする
    if db is not None:
        db.close()

# DBを使った関数の作成
@app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):
    # DBに接続
    db = get_db()
    curs = db.cursor()
    # テーブルを作成
    curs.execute(
        'CREATE TABLE IF NOT EXISTS persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
    db.commit()

    # URLから値を取得
    name = request.values.get('name', name)

    # GET
    if request.method == 'GET':
        # nameが入力されたら、そのnameでdb内を検索しにいく
        curs.execute('SELECT * FROM persons WHERE name = "{}"'.format(name))
        person = curs.fetchone()
        if not person:
            return "No", 404
        user_id, name = person
        # 結果と同時にステータスコードも返す
        return 'get {}:{}'.format(user_id, name), 200

    # POST
    if request.method == 'POST':
        # personsテーブルのnameカラムに入力された値を記録
        curs.execute('INSERT INTO persons(name) values("{}")'.format(name))
        db.commit()
        return 'created {}'.format(name), 200

    # PUT
    if request.method == 'PUT':
        # 値がなければエラーが返る　request.values.get()だと入力値がない場合は「None」が返される
        new_name = request.values['new_name']
        curs.execute('UPDATE persons set name = "{}" WHERE name = "{}"'.format(
            new_name, name))
        db.commit()
        return 'updated {}:{}'.format(name, new_name), 200

    # DELETE
    if request.method == 'DELETE':
        curs.execute('DELETE from persons WHERE name = "{}"'.format(name))
        db.commit()
        return 'delete {}'.format(name), 200

    curs.close()

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
