# tarfileの圧縮展開（zipファイルみたいなもの）
import tarfile

# 圧縮する際は'w:gz'とする
with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

# tarfileの展開
# tar zxvf test.tar.gz -C /tmp

# tarfileの読み込み（完全に展開してなかみの確認）
# with tarfile.open('test.tar.gz', 'r:gz') as tr:
#     tr.extractall(path='test_tar')

# tarfileの読み込み（中身のファイルの一部を確認）
with tarfile.open('test.tar.gz', 'r:gz') as tr:
    with tr.extractfile('test_dir/sub_dir/sub_dir.txt') as f:
        print(f.read())
