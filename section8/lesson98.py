# ファイル操作
# 大体以下のライブラリ名を覚えておいてGoogleで検索かければOK!
import os
import pathlib
import glob
import shutil

# このフォルダに'test.txt'があるか確認
print(os.path.exists('test.txt'))
print('##############')

# ファイルかどうか確認
print(os.path.isfile('test.txt'))
print('##############')

# ディレクトリかどうか確認
print(os.path.isdir('test.txt'))
print('##############')

# ファイルの名前を変更
os.rename('test.txt', 'renamed.txt')

# symlinkの作成(編集が同期するコピーファイルを生成)
os.symlink('renamed.txt', 'symlink.txt')

# ディレクトリの作成
os.mkdir('test_dir')

# ディレクトリの削除（ディレクトリの中に何も入ってなかったら）
os.rmdir('test_dir')

# 新しいファイルの作成
pathlib.Path('empty.txt').touch()

# ファイルの削除
os.remove('empty.txt')

# ディレクトリの中のディレクトリ一覧をを確認する
os.mkdir('test_dir')
os.mkdir('test_dir/test_dir2')
print(os.listdir('test_dir'))

# ディレクトリの中のファイル一覧を取得
pathlib.Path('test_dir/test_dir2/empty.txt').touch()
print(glob.glob('test_dir/test_dir2/*'))

# ファイルのコピー
shutil.copy('test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt')
print(glob.glob('test_dir/test_dir2/*'))

# ディレクトリの削除（中にファイルが有ってもOK!）
shutil.rmtree('test_dir')

# 現在のファイルの位置
print(os.getcwd())
