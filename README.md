
# どう使うの？
Docker Desktopをインストール後、
https://developers.io.net/docs/docker-installation-on-windows 
を参考にDockerを設定

.envファイルを作成
```
MYSQL_ROOT_PASSWORD=test

APPLICATION_DB_NAME=qpedia_test
APPLICATION_DB_USER=qpedia
APPLICATION_DB_PASS=pass
```


Windows PowerShellで次のコマンド

command:
```
docker-compose up -d
```

を実行すれば立ち上がるよ。

## 動作確認
うまくいったら次のURLで動作を確認できるよ [http://127.0.0.1](http://127.0.0.1:80) 

