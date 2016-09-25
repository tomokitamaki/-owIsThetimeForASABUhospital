# 概要
[麻生耳鼻咽喉科](http://www.jibiazabu.or.jp/azabu/index.html)の[待ち時間確認表示システム](http://konzatsu.net/sfd-m.php?cid=17514799)から指定の診察番号を拾ってきて、  
もうすぐ診察の順番が回ってくるようであればslackにお知らせしてくれる。  
判定は *[40]* などの[]を含む診察番号がページ内にあるかないかで判定をしています。  
診察番号が表示される個所にidなどのタグがないのでこういった方法をとっています。  

# 作った経緯
[待ち時間確認表示システム](http://konzatsu.net/sfd-m.php?cid=17514799)はメールでお知らせしてくれるものの、  
slackで通知してくれたほうが自分としては都合がいいので作りました。

# 使い方
1. このリポジトリをcloneする  
1. *webhookurlfile* というファイル名で中身はwebhookのURLというファイルを用意する。
```
ex)
#cat webhookurlfile
https://hooks.slack.com/services/asdfgh/jklmnbvcxz/qwertyuiop
```

2. NowIsThetimeForASABUhospital.pyを診察番号を第一引数として付与して実行する。  
```
ex) 診察番号が300の場合
python NowIsThetimeForASABUhospital.py 300
```

# 課題
slackでメンションつけて診察番号を投稿すると  
スクリプトが動くくらいにしないとちょっと面倒。  
