# 🧠 日本語 Word2Vec 体験アプリ

このアプリは、**日本語の単語同士の意味の関係を体験できるWebアプリ**です。  

## 🎯 目的

- 高校生向けに、「ベクトル同士の演算によって意味の関係が表現できる」ことなどを体験してもらう。
- このアプリをStreamlit経由でデプロイすると、ブラウザ上で簡単に操作できます。

## 🧪 できること

1. **類似語を調べる**  
　例：`青春` に似た単語を上位5つ表示

2. **単語間の類似度を調べる**  
　例：`ラーメン` と `パスタ` の類似度を数値で表示

3. **単語の足し算**  
　例：`公務員 + ピストル ≒？`

4. **単語の引き算**  
　例：`人生 - お金 ≒？`

5. **単語のアナロジー（比喩的関係）**  
　例：`王 - 男 + 女 ≒ 女王`

## 📦 使用しているモデルについて

- 使用モデル：日本語Wikipediaエンティティベクトル（300次元）
- 提供元：東北大学乾研究室
- モデルサイズ：約800MB

## 🔧 モデルのダウンロードについて

1. Dropbox（作者の私用スペース）から日本語モデルをダウンロード  
jawiki.word_vectors.300d.bin（約800MB）をDropboxから取得

2. 一時フォルダ /tmp/ に保存（ローカルにキャッシュされます）

3. モデルのロード  
gensimライブラリを使ってモデルを読み込みます

4. モデルのキャッシュ化  
@st.cache_resource を使ってStreamlitの再実行時に毎回ロードし直さないよう最適化

## ⚠️ 注意事項（モデルのダウンロードについて）

本アプリで使用している日本語Wikipediaエンティティベクトルは、開発者のDropboxアカウント上に一時的にホストされています。  
将来的にリンクが無効になる可能性があり、**モデルの永続的な提供は保証されていません。**

リンクが切れた場合は、お手数ですがご自身でモデルを用意して `app44.py` のURLを変更してください。


## 🪪 ライセンス

このプロジェクトは MIT ライセンスのもとで公開されています。 自由に利用・改変・再配布いただけますが、作者は一切の責任を負いません。 詳しくは LICENSE をご確認ください。

Copyright (c) 2024 かんたんAI教育ラボ
