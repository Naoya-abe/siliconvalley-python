from fabric.api import *
from fabric.contrib.files import *
from fabric.colors import green, red
# from fabric.api import run, env, roles, task, parallel, execute, runs_once

# hostとpassをあらかじめ記述しておく
env.hosts = ['root@172.16.200.101:22']
env.passwords = {'root@172.16.200.101:22': 'root'}
env.roledefs = {
    'common': ['root@172.16.200.101:22'],  # どのサーバーでも使う共通のものをインストールする
    'web': ['root@172.16.200.101:22'],
}


@task
@roles('common')
def install_package():  # 角サーバに共通のものは common を使ってインストールする
    # 次の行を実行するためのパッケージをインストール
    run('apt-get install -y software-properties-common')
    # この後にスーパーバイザーをインスト流する時に簡単にするために、repositoryを登録
    run('add-apt-repository universe')
    # updateしてuniverse使えるようにする
    run('apt-get update')
    # pythonのpipを使えるようにする
    run('apt-get install -y python-setuptools')
    # pipのインストール
    run('easy_install pip')


@task
@roles('web')
def deploy_web():
    run('apt-get install -y supervisor')
    run('apt-get install -y gunicorn')
    run('pip install Flask==0.12.2')
    if not exists('/root/work'):
        run('mkdir /root/work')

    # Flaskの実行ファイルをリモートへ
    put('roles/web/files/hello.py', '/root/work/hello.py')

    # supervisorの設定ファイルをリモートへ
    put('roles/web/files/app.conf', '/etc/supervisor/conf.d/app.conf')

    # supervisorを実行
    run('service supervisor restart')


@task
def deploy_dev_server():
    install_package()
    deploy_web()
    print(green('success'))
