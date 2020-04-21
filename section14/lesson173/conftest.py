#  conftestでは必ずconftest.pyを用意する
import os
import pytest


@pytest.fixture
def csv_file(tmpdir):
    # yieldを使うことで、テスト呼び出し先で、csv_faileを閉じる処理を記述しなくていい
    with open(os.path.join(tmpdir, 'test.csv'), 'w+') as c:
        print('before test')
        yield c
        print('after test')


def pytest_addoption(parser):
    # parserが引数
    parser.addoption('--os-name', default='linux', help='os name')
