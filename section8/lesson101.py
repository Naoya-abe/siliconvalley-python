# tempfile：一時ファイル（自動で削除される）
import tempfile

with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# ファイルを削除してほしくない場合
# with tempfile.NamedTemporaryFile(delete=False) as t:
#     print(t.name)
#     with open(t.name, 'w+') as f:
#         f.write('test\n')
#         f.seek(0)
#         print(f.read())

# 一時的にディレクトリを作
# 一時的にディレクトリを作って圧縮するといった使いみちがある
with tempfile.TemporaryDirectory() as td:
    print(td)

# 消されないディレクトリの作り方
temp_dir = tempfile.mkdtemp()
print(temp_dir)
