# lesson214で記述したfabfile.pyのコピー

from fabric.colors import green, red
import db.checking
from fabric.api import *
from fabric.contrib.files import *
# from fabric.api import run, env, roles, task, parallel, execute, runs_once

# hostとpassをあらかじめ記述しておく
env.hosts = ['root@172.16.200.101:22', 'root@172.16.200.102:22']
env.passwords = {
    'root@172.16.200.101:22': 'root',
    'root@172.16.200.102:22': 'root',
}
env.roledefs = {
    'web': ['root@172.16.200.101:22'],
    'db': ['root@172.16.200.102:22'],
}


@roles('web')  # デコレータでrolesをつけることで、指定した仮想サーバーのみにアクセスできる
def host_type():  # vagrant@main:/srv/ops/fab_project$ fab host_typeでterminalから実行可能
    run('uname -s')


@roles('db')
def host_files():
    run('ls -al')


def all_files():
    run('ls -al')


@task  # taskがつくと $ fab --list と入力した時に他の関数が隠れる
def go():  # taskを使うとfabコマンドで実行できる動作を限定している
    run('ls -al')


@task(default=True)  # defaultをTrueにすると、fabコマンドを入力した際にdefaultで表示される
def who():
    run('whoami')


@task
@parallel(pool_size=2)  # サーバーの同時実行（並列化）
def para():
    run('ls -al')


@task
def argtest(arg1, arg2):  # $ fab argtest:test1,test2 の形でterminalから引数を渡す
    print(arg1, arg2)


def test():
    return run('ls -al')


@task
def org():
    # test()の返り値を受け取ることができる
    r = execute(test)
    print(r)


@runs_once  # 1度だけ実行したい
def db_init():
    print('init')


@task
def deploy_db():
    db_init()
    db_init()  # @runs_onceがあれば、このように2回記述されても、1度しか実行されない


@task
def clean_and_upload():
    local('ls -al')
    # リモートにfabfileをコピーする
    put('fabfile.py', '/tmp/fabfile.py')
    with cd('/tmp'):
        run('pwd')
        run('ls -al')
        exists('/tmp/fabfile.py')


@task
def split_test():
    r = execute(db.checking.check)
    print(green(r))
    print(red('fail'))
    print(green('success'))
