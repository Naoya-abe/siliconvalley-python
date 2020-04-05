# zipファイルの圧縮確認
import zipfile


with zipfile.ZipFile('sample.zip', 'w') as z:
    # これだとフォルダしか作成されない
    z.write('sample_dir')
    z.write('sample_dir/sample_text.txt')

# terminal画面でzipファイルの解凍
# unzip sample.zip -d zzz
