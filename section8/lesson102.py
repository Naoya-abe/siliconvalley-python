# subprocessでコマンドを実行する
import subprocess

# 配列形式（基本こっち）
subprocess.run(['ls', '-a'])

# 配列形式がめんどくさい場合（セキュリティー的に推奨されていない）
subprocess.run('ls -a', shell=True)

# check=Trueをつけると、エラーがあった場合にExceptionが発生する
r = subprocess.run('lsaa', shell=True, check=True)
# エラーがない場合は0が表示される
print(r.returncode)
print('###')
