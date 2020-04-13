"""
SQLAlchemy
PythonのORMライブラリの一つ
RDBにアクセスするためのラッパー
SQLAlchemyを使って記述しておけば、sqliteとMySQLの置換が容易になる
オブジェクト指向的に簡単にDBにアクセスできる。SQL文を書かなくてもOK！
"""

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# 作業場所の作成 今回はsqliteのメモリ echo=True：sqlalchemyがどのようなSQL文を実行したか確認することができる
# engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

# 実際にDBを作成する時(sqlite)
# engine = sqlalchemy.create_engine('sqlite:///test_sqlite139.db', echo=True)

# 実際にDBを作成する時(mysql) pymysqlのインストール必要
# エラーがあったら公式リファレンスを読む：https://docs.sqlalchemy.org/en/13/core/engines.html
engine = sqlalchemy.create_engine(
    'mysql+pymysql://root@localhost/test_myswl_database139', echo=True)

# Baseクラスの作成
Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):  # Baseクラスを継承してテーブルを作成する
    __tablename__ = 'persons'  # クラス名は人1人を扱うオブジェクトなのでPersonだが
    id = sqlalchemy.Column(   # DBには複数のpersonデータが保存されるためtable_nameはpersons
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))


# engineに指定した環境でDBを作成する
Base.metadata.create_all(engine)

# DBにアクセスする
# Sessionの作成
Session = sqlalchemy.orm.sessionmaker(bind=engine)

# Sessionのオブジェクトを作成
session = Session()

# 挿入したいデータを記述
p1 = Person(name='Mike')
p2 = Person(name='Naoya')
p3 = Person(name='Takuya')

# DBに挿入
session.add(p1)
session.add(p2)
session.add(p3)

# 変更確定
session.commit()

# データ更新
# データ読み込み（個別） .first()：重複しているものがあったら、一番最初に検索に引っかかったものを返す
# p4はあくまでプログラム上の変数であり、実態は「id:1、name:Mike」のデータ
p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michel'
session.add(p4)
session.commit()

# データ削除
p5 = session.query(Person).filter_by(name='Takuya').first()
session.delete(p5)
session.commit()

# データの読み込み
persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
