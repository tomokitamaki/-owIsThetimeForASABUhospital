# 1. 目次

<!-- TOC -->

- [1. 目次](#1-目次)
- [2. 概要](#2-概要)
- [3. 作った経緯](#3-作った経緯)
- [4. 使い方](#4-使い方)
  - [4.1. 準備](#41-準備)
  - [4.2. 実行する](#42-実行する)
- [5. 課題](#5-課題)

<!-- /TOC -->

# 2. 概要

[麻生耳鼻咽喉科](http://www.jibiazabu.or.jp/azabu/index.html)の[待ち時間確認表示システム](http://konzatsu.net/sfd-m.php?cid=17514799)から指定の診察番号を拾ってきて、  
もうすぐ診察の順番が回ってくるようであればslackにお知らせしてくれる。  
判定は *[40]* などの[]を含む診察番号がページ内にあるかないかで判定をしています。  

# 3. 作った経緯

[待ち時間確認表示システム](http://konzatsu.net/sfd-m.php?cid=17514799)はメールでお知らせしてくれるものの、  
slackで通知してくれたほうが自分としては都合がいいので作りました。

# 4. 使い方

## 4.1. 準備

1. このリポジトリをcloneする  
1. *webhookurlfile.py* というファイルを作成する
1. 作成したwebhookurlfile.pyにwebhookのURLを記載する。  

~~~python
    ex)
    #cat webhookurlfile
    slack_url = https://hooks.slack.com/services/asdfgh/jklmnbvcxz/qwertyuiop
~~~

1. 必要なモジュールを入れておく

- requests  
  pip3 install requests
- BeautifulSoup  
  pip3 install beautifulsoup4

## 4.2. 実行する

1. NowIsThetimeForASABUhospital.pyを診察番号を第一引数として付与して実行する。  

~~~python
ex) 診察番号が300の場合
python3 NowIsThetimeForASABUhospital.py 300
~~~

# 5. 課題

slackでメンションつけて診察番号を投稿すると  
スクリプトが動くくらいにしないとちょっと面倒。  
