"""
mongoDBのインストール
https://reffect.co.jp/windows/mac-mongodb-install

brew tap mongodb/brew
==> Tapping mongodb/brew
Cloning into '/usr/local/Homebrew/Library/Taps/mongodb/homebrew-brew'...
remote: Enumerating objects: 113, done.
remote: Counting objects: 100% (113/113), done.
remote: Compressing objects: 100% (102/102), done.
remote: Total 172 (delta 51), reused 24 (delta 11), pack-reused 59
Receiving objects: 100% (172/172), 37.86 KiB | 271.00 KiB/s, done.
Resolving deltas: 100% (78/78), done.
Tapped 8 formulae (36 files, 93.4KB).
(base) ~/playground/python/siliconvalley-python/section12 $ brew install mongodb-community
Updating Homebrew...
==> Installing mongodb-community from mongodb/brew
==> Downloading https://fastdl.mongodb.org/osx/mongodb-macos

To have launchd start mongodb/brew/mongodb-community now and restart at login:
  brew services start mongodb/brew/mongodb-community
Or, if you don't want/need a background service you can just run:
  mongod --config /usr/local/etc/mongod.conf
==> Summary
🍺  /usr/local/Cellar/mongodb-community/4.2.5: 21 files, 305.9MB, built in 38 seconds
"""
