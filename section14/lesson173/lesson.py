"""
pytest-cov
テストのカバーしている範囲を出力してくれる
テストしていない箇所があったら出力してくれる

terminal
$ pip install pytest-cov pytest-xdist 

実行
$ pytest test_calculation.py --cov=calculation

ミスの箇所を確認
$ pytest test_calculation.py --cov=calculation --cov-report term-missing

if文は第1階層まで見れば基本OK
所属するチームに合わせる

https://docs.pytest.org/en/latest/contents.html
"""
