# biotype: peak extraction and smilarity evaluation

## フォルダの説明

- `biotype`: アルゴリズムを実装するPythonモジュールをまとめている。
- `doc` : 各種ドキュメントをまとめている。
- `extracted_peaks`: 下記の実験1で抽出されたピークをファイルに保存したもの。

## `biotype\similarity.py`

1. `similar_to()` :類似度を計算する関数。各種類似度計算をまとめたもの
2. `jaccard_similarity()` :Jaccard類似度を計算する関数
3. `rank_similarity()` :Rank類似度を計算する関数.`weighted=True`なら、重み付きRank類似度を計算する

## `biotype\peak_extract.py`

1. `find_peaks()` :ピークを抽出する関数。各種ピーク抽出手法をまとめたもの
2. `align()` :ピークアライメントを実現する関数。近似のピークに同じ`peak_id`を付与することで、`<peak_id, intensity>`のリストを返す。
3. `rank()` :`intensity`の高い順で`<peak_id, intensity>`から`<peak_id, rank>`に変換する関数。

## テストプログラム

1. 実験1(`test1_peak_extraction.ipynb`)，ピーク抽出、pickleファイル保存を行うノートブック。
2. 実験2(`test2_peak_alignment.ipynb`),ピークアライメントをテストするノートブック。
3. 実験3(`test3_similarity.ipynb`), 各種類似度計算をテストするノートブック。
4. 実験4(`test4_biotype.ipynb`), 各種菌株識別をテストするノートブック。
